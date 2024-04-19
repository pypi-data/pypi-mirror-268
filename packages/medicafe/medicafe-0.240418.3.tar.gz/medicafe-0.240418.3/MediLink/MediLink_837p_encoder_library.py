from datetime import datetime
import json
import requests
import time
import sys
import MediLink_ConfigLoader

"""
1. Code Refactoring: Increase modularity and clarity, particularly in segment creation functions (e.g., `create_st_segment`, `create_nm1_billing_provider_segment`), for better maintenance and readability.
2. Endpoint Support: Extend support within segment creation for additional endpoints with attention to their unique claim submission requirements.
3. Payer Identification Mechanism: Refine the mechanism for dynamically identifying payers, leveraging payer mappings and integrating with external APIs like Availity for precise payer information retrieval.
4. Adherence to Endpoint-Specific Standards: Implement and verify the compliance of claim data formatting and inclusion based on the specific demands of each target endpoint within the segment creation logic.
5. De-persisting Intermediate Files.
6. Get an API for Optum "Entered As". 
"""

# Logs messages with optional error type and claim data.
def log(message, config='', level="INFO", error_type=None, claim=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level = level.upper()  # Ensure the log level is in uppercase for consistency
    claim_data = "- Claim Data: {}\n".format(claim) if claim else ""
    error_info = "- Error Type: {}\n".format(error_type) if error_type else ""
    full_message = "[{}] {} - {} {} {}\n".format(timestamp, level, message, claim_data, error_info).strip()
    log_file_path = 'process_log.txt' if config == '' else config.get('logFilePath', 'process_log.txt')
    with open(log_file_path, 'a') as log_file:
        log_file.write(full_message)

# Converts date format from one format to another.
def convert_date_format(date_str):
    # Parse the input date string into a datetime object using the input format    
    # Determine the input date format based on the length of the input string
    input_format = "%m-%d-%Y" if len(date_str) == 10 else "%m-%d-%y"
    date_obj = datetime.strptime(date_str, input_format)
    # Format the datetime object into the desired output format and return
    return date_obj.strftime("%Y%m%d")

# Formats date and time according to the specified format.
def format_datetime(dt=None, format_type='date'):
    if dt is None:
        dt = datetime.now()
    if format_type == 'date':
        return dt.strftime('%Y%m%d')
    elif format_type == 'isa':
        return dt.strftime('%y%m%d')
    elif format_type == 'time':
        return dt.strftime('%H%M')

# Constructs the ST segment for transaction set.
def create_st_segment(transaction_set_control_number):
    return "ST*837*{:04d}*005010X222A1~".format(transaction_set_control_number)

# Constructs the BHT segment based on parsed data.
def create_bht_segment(parsed_data):
    chart_number = parsed_data.get('CHART', 'UNKNOWN')
    return "BHT*0019*00*{}*{}*{}*CH~".format(
        chart_number, format_datetime(), format_datetime(format_type='time'))
    
# Constructs the HL segment for billing provider.
def create_hl_billing_provider_segment():
    return "HL*1**20*1~"

# Constructs the NM1 segment for billing provider and includes address and Tax ID.
def create_nm1_billing_provider_segment(config, endpoint):
    endpoint_config = config['endpoints'].get(endpoint.upper(), {})
    
    # Billing provider details
    billing_provider_entity_code = endpoint_config.get('billing_provider_entity_code', '85')
    billing_provider_npi_qualifier = endpoint_config.get('billing_provider_npi_qualifier', 'XX')
    #billing_provider_lastname = endpoint_config.get('billing_provider_lastname', config.get('default_billing_provider_name', 'DEFAULT NAME'))
    #billing_provider_firstname = endpoint_config.get('billing_provider_firstname', '')
    billing_provider_lastname = config.get('billing_provider_lastname', config.get('default_billing_provider_name', 'DEFAULT NAME'))
    billing_provider_firstname = config.get('billing_provider_firstname', '')
    billing_provider_npi = endpoint_config.get('billing_provider_npi', config.get('default_billing_provider_npi', 'DEFAULT NPI'))
    
    # Determine billing_entity_type_qualifier based on the presence of billing_provider_firstname
    billing_entity_type_qualifier = '1' if billing_provider_firstname else '2'
    
    # Construct NM1 segment for the billing provider
    nm1_segment = "NM1*{}*{}*{}*{}****{}*{}~".format(
        billing_provider_entity_code, 
        billing_entity_type_qualifier,
        billing_provider_lastname, 
        billing_provider_firstname,
        billing_provider_npi_qualifier, 
        billing_provider_npi
    )
  
    # Construct address segments
    address_segments = []
    if config.get('billing_provider_address'):
        # N3 segment for address line
        address_segments.append("N3*{}~".format(config.get('billing_provider_address', 'NO ADDRESS')))
        # N4 segment for City, State, ZIP
        address_segments.append("N4*{}*{}*{}~".format(
            config.get('billing_provider_city', 'NO CITY'), 
            config.get('billing_provider_state', 'NO STATE'), 
            config.get('billing_provider_zip', 'NO ZIP')
        ))
    
    # Assuming Tax ID is part of the same loop, otherwise move REF segment to the correct loop
    ref_segment = "REF*EI*{}~".format(config.get('billing_provider_tin', 'NO TAX ID'))
    
    # Construct PRV segment if provider taxonomy is needed, are these just for Medicaid??
    #prv_segment = ""
    #if config.get('billing_provider_taxonomy'):
    #    prv_segment = "PRV*BI*PXC*{}~".format(config.get('billing_provider_taxonomy'))
    
    # Combine all the segments in the correct order, I think the PRV goes after the address and/or after ref
    segments = [nm1_segment]
    #if prv_segment:
    #    segments.append(prv_segment)
    segments.extend(address_segments)
    segments.append(ref_segment)
    
    return segments

# Constructs the NM1 segment and accompanying details for the service facility location.
def create_service_facility_location_npi_segment(config):
    """
    Constructs segments for the service facility location, including the NM1 segment for identification
    and accompanying N3 and N4 segments for address details.
    """
    facility_npi = config.get('service_facility_npi', 'DEFAULT FACILITY NPI')
    facility_name = config.get('service_facility_name', 'DEFAULT FACILITY NAME')
    address_line_1 = config.get('service_facility_address', 'NO ADDRESS')
    city = config.get('service_facility_city', 'NO CITY')
    state = config.get('service_facility_state', 'NO STATE')
    zip_code = config.get('service_facility_zip', 'NO ZIP')

    # NM1 segment for facility identification
    nm1_segment = "NM1*77*2*{}*****XX*{}~".format(facility_name, facility_npi)
    # N3 segment for facility address
    n3_segment = "N3*{}~".format(address_line_1)
    # N4 segment for facility city, state, and ZIP
    n4_segment = "N4*{}*{}*{}~".format(city, state, zip_code)

    return [nm1_segment, n3_segment, n4_segment]

# Constructs the NM1 segment for submitter name and includes PER segment for contact information.
def create_1000A_submitter_name_segment(config, endpoint):
    endpoint_config = config['endpoints'].get(endpoint.upper(), {})
    submitter_id_qualifier = endpoint_config.get('submitter_id_qualifier', '46')  # '46' for ETIN or 'XX' for NPI
    submitter_name = endpoint_config.get('nm_103_value', 'DEFAULT NAME')  # Default name if not in config
    submitter_id = endpoint_config.get('nm_109_value', 'DEFAULT ID')  # Default ID if not specified in endpoint
    
    # Submitter contact details
    contact_name = config.get('submitter_contact_name', 'RAFAEL OLIVERVIDAUD')
    contact_telephone_number = config.get('submitter_contact_tel', '9543821782')
    
    # Construct NM1 segment for the submitter
    nm1_segment = "NM1*41*2*{}*****{}*{}~".format(submitter_name, submitter_id_qualifier, submitter_id)
    
    # Construct PER segment for the submitter's contact information
    per_segment = "PER*IC*{}*TE*{}~".format(contact_name, contact_telephone_number)

    return [nm1_segment, per_segment]

# Constructs the NM1 segment for the receiver (1000B).
def create_1000B_receiver_name_segment(config, endpoint):
    # Retrieve endpoint specific configuration
    endpoint_config = config['endpoints'].get(endpoint.upper(), {})

    # Set the entity identifier code to '40' for receiver and qualifier to '46' for EDI, 
    # unless specified differently in the endpoint configuration.
    receiver_entity_code = '40'
    receiver_id_qualifier = endpoint_config.get('receiver_id_qualifier', '46')
    receiver_name = endpoint_config.get('receiver_name', 'DEFAULT RECEIVER NAME')
    receiver_edi = endpoint_config.get('receiver_edi', 'DEFAULT EDI')
    
    return "NM1*{entity_code}*2*{receiver_name}*****{id_qualifier}*{receiver_edi}~".format(
        entity_code=receiver_entity_code,
        receiver_name=receiver_name,
        id_qualifier=receiver_id_qualifier,
        receiver_edi=receiver_edi
    )

def map_insurance_name_to_payer_id(insurance_name, config):
    """
    Maps the insurance name provided by Medisoft to the corresponding payer ID by referencing
    a crosswalk mapping stored in the "crosswalk" JSON file. This file must be located at a path
    specified in the config under the key 'crosswalk_path'.

    Inputs:
    - insurance_name: The name of the insurance as provided by Medisoft.

    Outputs:
    - payer_id: The unique identifier (ID) corresponding to the insurance name, if the mapping
      is successful. It will be a 5-character alphanumeric code.

    Functionality:
    - This function retrieves the mapping from a "crosswalk" JSON file.
    - If the mapping is successful, it returns the payer ID.
    - If the mapping fails or the payer ID cannot be retrieved, it raises an error indicating
      the inability to extract the payer ID.
    """
    _, crosswalk = MediLink_ConfigLoader.load_configuration(None, config.get('crosswalkPath', 'crosswalk.json'))
    
    try:
        payer_id = crosswalk['medisoft_insurance_to_payer_id'].get(insurance_name)
        if not payer_id:
            raise ValueError("No payer ID found for insurance name: {}".format(insurance_name))
        return payer_id
    except json.JSONDecodeError:
        raise ValueError("Error decoding the crosswalk JSON file")

def fetch_payer_name_from_crosswalk(payer_id, config, endpoint):
    """
    Retrieves the payer name corresponding to a given payer ID from a crosswalk mapping.
    
    Parameters:
    - payer_id: The unique identifier for the payer whose name is to be resolved.
    - config: Configuration dictionary including the path to the crosswalk JSON.
    
    Returns:
    - The payer name corresponding to the payer ID.
    
    Raises:
    - ValueError if the payer ID is not found in the crosswalk mapping.
    """
    # Ensure the 'crosswalkPath' key exists in config and contains the path to the crosswalk JSON file
    if 'crosswalkPath' not in config:
        raise ValueError("Crosswalk path not defined in configuration.")

    crosswalk_path = config.get('crosswalkPath')
    try:
        with open(crosswalk_path, 'r') as file:
            crosswalk_mappings = json.load(file)
        # Select the endpoint-specific section from the mappings
        endpoint_mappings = crosswalk_mappings['payer_id_to_name'].get(endpoint, {})
        payer_name = endpoint_mappings.get(payer_id)

        if not payer_name:
            raise ValueError("Payer name not found for payer ID: {} in {} mappings.".format(payer_id, endpoint))

        return payer_name
    except FileNotFoundError:
        raise FileNotFoundError("Crosswalk file not found at {}".format(crosswalk_path))
    except json.JSONDecodeError as e:
        raise ValueError("Error decoding the crosswalk JSON file: {}".format(e))

def create_2010BB_payer_information_segment(parsed_data, config, endpoint):
    """
    Dynamically generates the NM1 segment for the payer in the 2010BB loop of an 837P transaction.
    This process involves mapping the insurance name to the correct payer ID and then resolving the payer name.
    The function prioritizes the Availity API for payer name resolution (currently the only API integrated) 
    and falls back to crosswalk mapping if necessary or when additional APIs are not available.
    
    Parameters:
    - parsed_data: Dictionary containing parsed claim data, including the insurance name.
    - config: Configuration dictionary including endpoint-specific settings and crosswalk paths.
    - endpoint: Target endpoint for submission, e.g., 'Availity'. Future integrations may include 'Optum', 'PNT_DATA'.

    Returns:
    - A formatted NM1*PR segment string for the 2010BB loop, correctly identifying the payer with its name and ID.

    Process:
    1. Maps the insurance name to a payer ID using a crosswalk mapping or configuration.
    2. Attempts to resolve the payer name using the Availity API based on the payer ID.
    3. Falls back to crosswalk mapping for payer name resolution if the API call fails or is not applicable.
    
    Raises an error if the payer ID extraction or payer name resolution fails, ensuring transaction integrity.
    
    A reference for a payer ID to payer name mapping for Optum can be found here:
    https://iedi.optum.com/iedi/enspublic/Download/Payerlists/Medicalpayerlist.pdf
    This or similar resources could be used to populate the initial configuration mapping.
    """
    # Step 1: Map insurance name to Payer ID
    insurance_name = parsed_data.get('INAME', '')
    payer_id = map_insurance_name_to_payer_id(insurance_name, config)

    payer_name = ''
    # Step 2: Attempt to Retrieve Payer Name from Availity API (current API integration)
    endpoint = 'availity' # Force availity API because none of the other ones are connected BUG
    if True: #endpoint.lower() == 'availity':
        try:
            payer_name = fetch_payer_name_from_api(payer_id, config, endpoint)
            log("Resolved payer name {} via {} API for Payer ID: {}".format(payer_name, endpoint, payer_id), config, level="INFO")
        except Exception as api_error:
            print("{} API call failed for Payer ID '{}': {}".format(endpoint, payer_id, api_error))

    # Placeholder for future API integrations with other endpoints
    # elif endpoint.lower() == 'optum':
    #     payer_name = fetch_payer_name_from_optum_api(payer_id, config)
    # elif endpoint.lower() == 'pnt_data':
    #     payer_name = fetch_payer_name_from_pnt_data_api(payer_id, config)

    # Step 3: Fallback to Crosswalk Mapping if API resolution fails or is not applicable
    if not payer_name:
        payer_name = fetch_payer_name_from_crosswalk(payer_id, config, endpoint)

    # Construct and return the NM1*PR segment for the 2010BB loop with the payer name and ID
    # Is this supposed to be PI instead of PR?
    return "NM1*PR*2*{}*****PI*{}~".format(payer_name, payer_id)

def create_nm1_payto_address_segments(config):
    """
    Constructs the NM1 segment for the Pay-To Address, N3 for street address, and N4 for city, state, and ZIP.
    This is used if the Pay-To Address is different from the Billing Provider Address.
    """
    payto_provider_name = config.get('payto_provider_name', 'DEFAULT PAY-TO NAME')
    payto_address = config.get('payto_address', 'DEFAULT PAY-TO ADDRESS')
    payto_city = config.get('payto_city', 'DEFAULT PAY-TO CITY')
    payto_state = config.get('payto_state', 'DEFAULT PAY-TO STATE')
    payto_zip = config.get('payto_zip', 'DEFAULT PAY-TO ZIP')

    nm1_segment = "NM1*87*2*{}~".format(payto_provider_name)  # '87' indicates Pay-To Provider
    n3_segment = "N3*{}~".format(payto_address)
    n4_segment = "N4*{}*{}*{}~".format(payto_city, payto_state, payto_zip)

    return [nm1_segment, n3_segment, n4_segment]

def create_payer_address_segments(config):
    """
    Constructs the N3 and N4 segments for the payer's address.
    
    """
    payer_address_line_1 = config.get('payer_address_line_1', '')
    payer_city = config.get('payer_city', '')
    payer_state = config.get('payer_state', '')
    payer_zip = config.get('payer_zip', '')

    n3_segment = "N3*{}~".format(payer_address_line_1)
    n4_segment = "N4*{}*{}*{}~".format(payer_city, payer_state, payer_zip)

    return [n3_segment, n4_segment]

# Fetches the payer name from API based on the payer ID.
# Initialize a global dictionary to store the access token and its expiry time
# BUG This will need to get setup for each endpoint separately. 
token_cache = {
    'access_token': None,
    'expires_at': 0  # Timestamp of when the token expires
}

def get_access_token(endpoint_config):
    current_time = time.time()
    
    # Check if the cached token is still valid
    if token_cache['access_token'] and token_cache['expires_at'] > current_time:
        return token_cache['access_token']

    # Validate endpoint configuration
    if not endpoint_config or not all(k in endpoint_config for k in ['client_id', 'client_secret', 'token_url']):
        raise ValueError("Endpoint configuration is incomplete or missing necessary fields.")

    # Extract credentials and URL from the config
    CLIENT_ID = endpoint_config.get("client_id")
    CLIENT_SECRET = endpoint_config.get("client_secret")
    url = endpoint_config.get("token_url")

    # Setup the data payload and headers for the HTTP request
    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope': 'hipaa'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        # Perform the HTTP request to get the access token
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # This will raise an exception for HTTP error statuses
        json_response = response.json()
        access_token = json_response.get('access_token')
        expires_in = json_response.get('expires_in', 3600)  # Default to 3600 seconds if not provided

        if not access_token:
            raise ValueError("No access token returned by the server.")
        
        # Store the access token and calculate the expiry time
        token_cache['access_token'] = access_token
        token_cache['expires_at'] = current_time + expires_in - 120  # Subtracting 120 seconds to provide buffer

        return access_token
    except requests.RequestException as e:
        # Handle HTTP errors (e.g., network problems, invalid response)
        error_msg = "Failed to retrieve access token: {0}. Response status: {1}".format(str(e), response.status_code if response else 'No response')
        raise Exception(error_msg)
    except ValueError as e:
        # Handle specific errors like missing access token
        raise Exception("Configuration or server response error: {0}".format(str(e)))

def fetch_payer_name_from_api(payer_id, config, endpoint):
    
    endpoint_config = config['endpoints'].get(endpoint.upper(), {})
    # Currently configured for Availity
    token = get_access_token(endpoint_config)  # Get the access token using the function above
       
    api_url = endpoint_config.get("api_url", "")
    headers = {
        'Authorization': 'Bearer {0}'.format(token),
        'Accept': 'application/json'
    }
    params = {'payerId': payer_id}
    # print(params) DEBUG

    try:
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()
        # print(data) DEBUG
                
        # Check if 'payers' key exists and has at least one item
        if 'payers' in data and data['payers']:
            payer = data['payers'][0]
            payer_name = payer.get('displayName') or payer.get('name', 'No name available')
            return payer_name
        else:
            raise ValueError("No payer found for ID: {0}".format(payer_id))
    except requests.RequestException as e:
        print("Error fetching payer name: {0}".format(e))
        raise

# Test Case for API fetch
#payer_id = "11347"
#config = load_configuration() 
#payer_name = fetch_payer_name_from_api(payer_id, config, endpoint='AVAILITY')
#print(payer_id, payer_name)

# Constructs the PRV segment for billing provider.
def create_billing_prv_segment(config, endpoint):
    if endpoint.lower() == 'optumedi':
        return "PRV*BI*PXC*{}~".format(config['billing_provider_taxonomy'])
    return ""

# Constructs the HL segment for subscriber [hierarchical level (HL*2)]
def create_hl_subscriber_segment():
    return ["HL*2*1*22*0~"]

# Constructs the SBR segment for subscriber based on parsed data and configuration.
def create_sbr_segment(config, parsed_data, endpoint):
    # Determine the payer responsibility sequence number code based on the payer type
    # If the payer is Medicare, use 'P' (Primary)
    # If the payer is not Medicare and is primary insurance, use 'P' (Primary)
    # If the payer is secondary insurance after Medicare, use 'S' (Secondary)
    # For simplicity, we're going to assume everything is Primary for now.
    responsibility_code = 'P'

    # Determine the insurance type code based on the payer
    # Map different payers to their respective insurance type codes
    # For simplicity, 'CI' (Commercial Insurance) as a default
    insurance_type_code = 'CI'

    # Construct the SBR segment using the determined codes
    sbr_segment = "SBR*{responsibility_code}*18*******{insurance_type_code}~".format(
        responsibility_code=responsibility_code,
        insurance_type_code=insurance_type_code
    )

    return sbr_segment

# Constructs the NM1 segment for subscriber based on parsed data and configuration.
def create_nm1_subscriber_segment(config, parsed_data, endpoint):
    if endpoint.lower() == 'optumedi':
        entity_identifier_code = config['endpoints']['OPTUMEDI'].get('subscriber_entity_code', 'IL')
    else:
        entity_identifier_code = 'IL'  # Default value if endpoint is not 'optumedi'

    return "NM1*{entity_identifier_code}*1*{last_name}*{first_name}*{middle_name}***MI*{policy_number}~".format(
        entity_identifier_code=entity_identifier_code,
        last_name=parsed_data['LAST'],
        first_name=parsed_data['FIRST'],
        middle_name=parsed_data['MIDDLE'],
        policy_number=parsed_data['IPOLICY']
    )

# Constructs the N3 and N4 segments for subscriber address based on parsed data.
def create_subscriber_address_segments(parsed_data):
    return [
        "N3*{}~".format(parsed_data['ISTREET']),
        "N4*{}*{}*{}~".format(
            parsed_data['ICITY'],  
            parsed_data['ISTATE'],  
            parsed_data['IZIP'][:5]
        )
    ]

# Constructs the DMG segment for subscriber based on parsed data.
def create_dmg_segment(parsed_data):
    return "DMG*D8*{}*{}~".format(
        convert_date_format(parsed_data['BDAY']),  
        parsed_data['SEX'] # ensure it returns a string instead of a list if it only returns one segment
    )

def create_nm1_rendering_provider_segment(config, is_rendering_provider_different=False):
    """
    #BUG This is getting placed incorrectly.
    
    Constructs the NM1 segment for the rendering provider in the 2310B loop using configuration data.
    
    Parameters:
    - config: Configuration dictionary including rendering provider details.
    - is_rendering_provider_different: Boolean indicating if rendering provider differs from billing provider.
    
    Returns:
    - List containing the NM1 segment for the rendering provider if required, otherwise an empty list.
    """
    if is_rendering_provider_different:
        segments = []
        rp_npi = config.get('rendering_provider_npi', '')
        rp_last_name = config.get('rendering_provider_last_name', '')
        rp_first_name = config.get('rendering_provider_first_name', '')

        # NM1 Segment for Rendering Provider
        segments.append("NM1*82*1*{0}*{1}**XX*{2}~".format(
            rp_last_name, 
            rp_first_name, 
            rp_npi
        ))
        
        # PRV Segment for Rendering Provider Taxonomy
        if config.get('rendering_provider_taxonomy'):
            segments.append("PRV*PE*PXC*{}~".format(config['billing_provider_taxonomy']))
        
        return segments
    else:
        return []

def format_claim_number(chart_number, date_of_service):
    # Remove any non-alphanumeric characters from chart number and date
    chart_number_alphanumeric = ''.join(filter(str.isalnum, chart_number))
    date_of_service_alphanumeric = ''.join(filter(str.isalnum, date_of_service))
    
    # Combine the alphanumeric components without spaces
    formatted_claim_number = chart_number_alphanumeric + date_of_service_alphanumeric
    
    return formatted_claim_number

# Constructs the CLM and related segments based on parsed data and configuration.
def create_clm_and_related_segments(parsed_data, config):
    """
    Insert the claim information (2300 loop), 
    ensuring that details such as claim ID, total charge amount,and service date are included.
    
    The HI segment for Health Care Diagnosis Codes should accurately reflect the diagnosis related to the service line.
    
    Service Line Information (2400 Loop):
    Verify that the service line number (LX), professional service (SV1), and service date (DTP) segments contain
    accurate information and are formatted according to the claim's details.
    """
    
    segments = []
    
    # Format the claim number
    chart_number = parsed_data.get('CHART', '')
    date_of_service = parsed_data.get('DATE', '')
    formatted_claim_number = format_claim_number(chart_number, date_of_service)
        
    # CLM - Claim Information
    segments.append("CLM*{}*{}***{}:B:1*Y*A*Y*Y~".format(
        formatted_claim_number,
        parsed_data['AMOUNT'],
        parsed_data['TOS']))
    
    # HI - Health Care Diagnosis Code
    # The code value should be preceded by the qualifier "ABK" or "BK" to specify the type of 
    # diagnosis code being used. "ABK" typically indicates ICD-10 codes, while "BK" indicates ICD-9 codes.
    segments.append("HI*ABK:H{}~".format(''.join(char for char in parsed_data['DIAG'] if char.isalnum() or char.isdigit())))
    
    # (2310C Loop) Service Facility Location NPI and Address Information
    segments.extend(create_service_facility_location_npi_segment(config))
    
    # For future reference, SBR - (Loop 2320: OI, NM1 (2330A), N3, N4, NM1 (2330B)) - Other Subscriber Information goes here.
    
    # LX - Service Line Number
    segments.append("LX*1~")
    
    # SV1 - Professional Service
    segments.append("SV1*HC:{}:{}*{}*MJ*{}***1~".format(
        parsed_data['CODEA'],
        parsed_data['POS'],
        parsed_data['AMOUNT'],
        parsed_data['MINTUES']))
    
    # DTP - Date
    segments.append("DTP*472*D8*{}~".format(convert_date_format(parsed_data['DATE'])))
    
    # Is there REF - Line Item Control Number missing here?
    
    return segments

# Generates the ISA and GS segments for the interchange header based on configuration and endpoint.
def create_interchange_header(config, endpoint):
    """
    Generate ISA and GS segments for the interchange header, ensuring endpoint-specific requirements are met.
    Includes support for Availity, Optum, and PNT_DATA endpoints, with streamlined configuration and default handling.

    Parameters:
    - config: Configuration dictionary with settings and identifiers.
    - endpoint: String indicating the target endpoint ('Availity', 'Optum', 'PNT_DATA').

    Returns:
    - Tuple containing the ISA and GS segment strings.
    """
    endpoint_config = config['endpoints'].get(endpoint.upper(), {})
    
    # Set defaults for ISA segment values
    isa02 = isa04 = "          "  # Default value for ISA02 and ISA04
    isa05 = isa07 = 'ZZ'  # Default qualifier
    isa13 = '000000001' # Default Interchange Control Number. Not sure what to do with this. date? See also trailer
    isa15 = 'P'  # 'T' for Test, 'P' for Production
    
    # Conditional values from config
    isa_sender_id = endpoint_config.get('isa_06_value', config.get('submitterId', '')).rstrip()
    isa07_value = endpoint_config.get('isa_07_value', isa07)
    isa_receiver_id = endpoint_config.get('isa_08_value', config.get('receiverId', '')).rstrip()
    isa13_value = endpoint_config.get('isa_13_value', isa13) # Needs to match IEA02
    gs_sender_code = endpoint_config.get('gs_02_value', config.get('submitterEdi', ''))
    gs_receiver_code = endpoint_config.get('gs_03_value', config.get('receiverEdi', ''))
    isa15_value = endpoint_config.get('isa_15_value', isa15)

    # ISA Segment
    isa_segment = "ISA*00*{}*00*{}*{}*{}*{}*{}*{}*{}*^*00501*{}*0*{}*:~".format(
        isa02, isa04, isa05, isa_sender_id.ljust(15), isa07_value, isa_receiver_id.ljust(15),
        format_datetime(format_type='isa'), format_datetime(format_type='time'), isa13_value, isa15_value
    )

    # GS Segment
    # GS04 YYYYMMDD
    # GS06 Group Control Number, Field Length 1/9, must match GE02
    gs06 = '1' # Placeholder for now?
    
    gs_segment = "GS*HC*{}*{}*{}*{}*{}*X*005010X222A1~".format(
        gs_sender_code, gs_receiver_code, format_datetime(), format_datetime(format_type='time'), gs06
    )

    log("Created interchange header for endpoint: {}".format(endpoint), config, level="INFO")
    
    return isa_segment, gs_segment

# Generates the GE and IEA segments for the interchange trailer based on the number of transactions and functional groups.
def create_interchange_trailer(config, endpoint, num_transactions, num_functional_groups=1):
    """
    Generate GE and IEA segments for the interchange trailer.
    
    Parameters:
    - num_transactions: The number of transactions within the functional group.
    - num_functional_groups: The number of functional groups within the interchange. Default is 1.
    
    Returns:
    - Tuple containing the GE and IEA segment strings.
    """
    endpoint_config = config['endpoints'].get(endpoint.upper(), {})
    # GE Segment: Functional Group Trailer
    # Indicates the end of a functional group and provides the count of the number of transactions within it.
    # GE02 Group Control Number, Field Length 1/9, must match GS06 (Header)
    ge02 = '1' #Placeholder for now?
    ge_segment = "GE*{}*{}~".format(num_transactions, ge02)
    
    # IEA Segment: Interchange Control Trailer
    isa13 = '000000001' # Default Interchange Control Number. Not sure what to do with this. date? See also trailer
    isa13_value = endpoint_config.get('isa_13_value', isa13) # Needs to match IEA02, can this be a date/time?
    # Indicates the end of an interchange and provides the count of the number of functional groups within it.
    # The Interchange Control Number needs to match isa13 and iea02
    iea_segment = "IEA*{}*{}~".format(num_functional_groups, isa13_value)
    
    log("Created interchange trailer", config, level="INFO")
    
    return ge_segment, iea_segment

# Generates segment counts for the formatted 837P transaction and updates SE segment.
def generate_segment_counts(compiled_segments, transaction_set_control_number):
    # Count the number of segments, not including the placeholder SE segment
    segment_count = compiled_segments.count('~')   # + 1 Including SE segment itself, but seems to be giving errors.
    
    # Ensure transaction set control number is correctly formatted as a string
    formatted_control_number = str(transaction_set_control_number).zfill(4)  # Pad to ensure minimum 4 characters

    # Construct the SE segment with the actual segment count and the formatted transaction set control_number
    se_segment = "SE*{0}*{1}~".format(segment_count, formatted_control_number)

    # Assuming the placeholder SE segment was the last segment added before compiling
    # This time, we directly replace the placeholder with the correct SE segment
    formatted_837p = compiled_segments.rsplit('SE**', 1)[0] + se_segment
    
    return formatted_837p