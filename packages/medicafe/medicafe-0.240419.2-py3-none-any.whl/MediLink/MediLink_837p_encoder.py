import re
from datetime import datetime
import argparse
import os
import MediLink_837p_encoder_library
import MediLink_ConfigLoader
from MediLink_DataMgmt import parse_fixed_width_data, read_fixed_width_data
#from tqdm import tqdm

"""
Development Task List:

1. File Path Management: Enhance the handling of input paths to efficiently manage both individual files and directories, accommodating a range of file processing scenarios.
2. User Interface Improvement: Advance the CLI for intuitive user interaction, offering clear options for file processing and real-time progress updates.
3. Validation and Logging: Strengthen validation processes for input data, incorporating thorough checks against business rules and enhanced detailed logging for improved traceability and troubleshooting.
4. Batch Processing and Output Handling: Enhance output file management to support efficient batch operations, including systematic naming and organization for output files.
5. Comprehensive Documentation: Maintain up-to-date and detailed documentation within the codebase, ensuring all functions and complex logic are clearly explained.
6. De-persisting Intermediate Files.
"""
def create_interchange_elements(config, endpoint, transaction_set_control_number):
    """
    Create interchange headers and trailers for an 837P document.

    Parameters:
    - config: Configuration settings loaded from a JSON file.
    - endpoint_key: The endpoint for which the data is being processed.
    - transaction_set_control_number: The starting transaction set control number.

    Returns:
    - Tuple containing (ISA header, GS header, GE trailer, IEA trailer).
    """
    isa_header, gs_header = MediLink_837p_encoder_library.create_interchange_header(config, endpoint)
    ge_trailer, iea_trailer = MediLink_837p_encoder_library.create_interchange_trailer(config, endpoint, transaction_set_control_number)
    return isa_header, gs_header, ge_trailer, iea_trailer

def format_single_claim(patient_data, config, endpoint, transaction_set_control_number):
    """
    Formats a single claim into 837P segments based on the provided patient data and endpoint.
    
    Parameters:
    - patient_data: Dictionary containing detailed patient data.
    - config: Configuration settings loaded from a JSON file.
    - endpoint: The endpoint key representing the specific endpoint.
    - transaction_set_control_number: Starting transaction set control number for 837P segments.
    
    Returns:
    - String representation of the formatted 837P claim.
    """
    segments = []
        
    # Initialize with standard segments for all claims
    segments.append(MediLink_837p_encoder_library.create_st_segment(transaction_set_control_number))
    segments.append(MediLink_837p_encoder_library.create_bht_segment(patient_data))

    # Submitter Name Segment and PER Contact Information (1000A Loop)
    segments.extend(MediLink_837p_encoder_library.create_1000A_submitter_name_segment(config, endpoint))
    
    # Receiver Name Segment (1000B Loop)
    segments.extend([MediLink_837p_encoder_library.create_1000B_receiver_name_segment(config, endpoint)])
    
    # Billing Provider Segments (2010AA Loop)
    segments.extend([MediLink_837p_encoder_library.create_hl_billing_provider_segment()])
    segments.extend(MediLink_837p_encoder_library.create_nm1_billing_provider_segment(config, endpoint))

    # Pay-To Address Segment (2010AB Loop) if the Pay-To Address differs from the Billing Provider's address
    #segments.extend(MediLink_837p_encoder_library.create_nm1_payto_address_segments(config))
    
    # PRV Provider Taxonomy Segment
    #segments.extend([MediLink_837p_encoder_library.create_billing_prv_segment(config, endpoint)])
    
    # Subscriber information, possibly including endpoint-specific logic
    segments.extend(MediLink_837p_encoder_library.create_hl_subscriber_segment())
    segments.append(MediLink_837p_encoder_library.create_sbr_segment(config, patient_data, endpoint))
    segments.append(MediLink_837p_encoder_library.create_nm1_subscriber_segment(config, patient_data, endpoint))
    segments.extend(MediLink_837p_encoder_library.create_subscriber_address_segments(patient_data))
    segments.append(MediLink_837p_encoder_library.create_dmg_segment(patient_data))
    
    # Payer information (2010BB loop)
    segments.extend([MediLink_837p_encoder_library.create_2010BB_payer_information_segment(patient_data, config, endpoint)])
    #segments.extend(MediLink_837p_encoder_library.create_payer_address_segments(config)) OMITTED
    
    # Rendering Provider (2310B Loop)
    segments.extend(MediLink_837p_encoder_library.create_nm1_rendering_provider_segment(config))
    
    # Claim information 2300, 2310C Service Facility and 2400 loop segments
    segments.extend(MediLink_837p_encoder_library.create_clm_and_related_segments(patient_data, config))

    # Placeholder for the SE segment to be updated with actual segment count later
    segments.append("SE**{transaction_set_control_number:04d}~")

    # Update SE segment with the actual segment count and generate the final formatted 837P string
    formatted_837p = MediLink_837p_encoder_library.generate_segment_counts('\n'.join(filter(None, segments)), transaction_set_control_number)

    # Optionally, print or log the formatted 837P for debugging or verification
    # BUG Add chart number to this.
    MediLink_837p_encoder_library.log("Formatted 837P for endpoint {}.".format(endpoint), config, level="INFO")

    return formatted_837p

def write_output_file(document_segments, output_directory, endpoint_key, input_file_path, config):
    """
    Writes formatted 837P document segments to an output file with a dynamically generated name.
    
    Development Roadmap:
    - Ensure input `document_segments` is a non-empty list to avoid creating empty files.
    - Verify `output_directory` exists and is writable before proceeding. Create the directory if it does not exist.
    - Consider parameterizing the file naming convention or providing options for customization to accommodate different organizational needs.
    - Implement error handling to gracefully manage file writing failures, potentially returning a status or error message alongside the file path.
    - Incorporate logging directly within the function, accepting an optional `config` or `logger` parameter to facilitate tracking of the file writing process and outcomes.
    - Update the return value to include both the path to the output file and any relevant status information (e.g., success flag, error message) to enhance downstream error handling and user feedback.
    
    Parameters:
    - document_segments: List of strings, where each string is a segment of the 837P document to be written.
    - output_directory: String specifying the directory where the output file will be saved.
    - endpoint_key: String specifying the endpoint for which the claim is processed, used in naming the output file.
    - input_file_path: String specifying the path to the input file being processed, used in naming the output file.
    
    Returns:
    - String specifying the path to the successfully created output file. Consider returning a tuple (path, status) for enhanced error handling.
    """
    formatted_837p = '\n'.join(document_segments)
    base_name = os.path.splitext(os.path.basename(input_file_path))[0]
    timestamp = datetime.now().strftime("%m%d%H%M")
    new_output_file_name = "{}_{}_{}.txt".format(base_name, endpoint_key.lower(), timestamp)
    new_output_file_path = os.path.join(output_directory, new_output_file_name)

    with open(new_output_file_path, 'w') as output_file:
        output_file.write(formatted_837p)

    # need to pass config here. for what?   
    # BUG Validate that the output file path has no spaces in it, Unless this is no issue (skip)
    MediLink_837p_encoder_library.log("Successfully converted and saved to {}".format(new_output_file_path), config, level="INFO")
    
    return new_output_file_path

def process_file(file_path, config, endpoint_key, transaction_set_control_number):
    """
    Reads, validates, and formats claim data from a given file into the 837P format.

    :param file_path: The path to the file containing claim data.
    :param config: Configuration settings loaded from a JSON file.
    :param endpoint_key: The key representing the endpoint for which the claim is being processed.
    :param transaction_set_control_number: The starting transaction set control number for 837P segments.
    :return: A tuple containing the formatted claim segments and the next transaction set control number.
    """
    formatted_claims = []
    
    for personal_info, insurance_info, service_info in read_fixed_width_data(file_path, config):
        # Parse and validate claim data
        parsed_data = parse_fixed_width_data(personal_info, insurance_info, service_info, config)
        
        # Assume validate_claim_data is a function that validates the parsed data
        # DISABLED
        #if not validate_claim_data(parsed_data, config):
        #    MediLink_837p_encoder_library.log("Validation failed for claim data in file: {}".format(file_path), config, level="ERROR")
        #    continue  # Skip invalid claims

        # Format the claim into 837P segments
        formatted_claim = format_single_claim(parsed_data, config, endpoint_key, transaction_set_control_number)
        formatted_claims.append(formatted_claim)
        transaction_set_control_number += 1  # Increment for each successfully processed claim

    # Combine all formatted claims into a single string to be appended to the document segments
    formatted_claims_str = '\n'.join(formatted_claims)
        
    return formatted_claims_str, transaction_set_control_number

def winscp_validate_output_directory(output_directory):
    """
    Validates the output directory path to ensure it has no spaces.
    If spaces are found, prompts the user to input a new path.
    If the directory doesn't exist, creates it.
    """
    while ' ' in output_directory:
        print("\nWARNING: The output directory path contains spaces, which can cause issues with upload operations.")
        print("    Current proposed path: {}".format(output_directory))
        new_path = input("Please enter a new path for the output directory: ")
        output_directory = new_path.strip()  # Remove leading/trailing spaces
    
    # Check if the directory exists, if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print("INFO: Created output directory: {}".format(output_directory))
    
    return output_directory

def convert_files_for_submission(detailed_patient_data, config):
    """    
    Processes detailed patient data for submission based on their confirmed endpoints,
    generating a separate 837P file for each endpoint.

    Parameters:
    - detailed_patient_data: A list containing detailed patient data with endpoint information.
    - config: Configuration settings loaded from a JSON file.

    Returns:
    - A list of paths to the converted files ready for submission.
    """

    # Initialize a dictionary to hold patient data segregated by confirmed endpoints
    data_by_endpoint = {}
        
    # Populate the dictionary with patient data
    for data in detailed_patient_data:
        endpoint = data['confirmed_endpoint']
        if endpoint not in data_by_endpoint:
            data_by_endpoint[endpoint] = []
        data_by_endpoint[endpoint].append(data)

    # List to store paths of converted files for each endpoint
    converted_files_paths = []

    # Determine the total number of unique endpoints for progress bar
    # total_endpoints = len(data_by_endpoint)

    # Iterate over each endpoint and process its corresponding patient data
    for endpoint, patient_data_list in data_by_endpoint.items():
        # tqdm(data_by_endpoint.items(), desc="Creating 837p(s)", total=total_endpoints, ascii=True)
        # Each endpoint might have multiple patients' data to be processed into a single 837P file
        if patient_data_list:
            converted_path = process_claim(config['MediLink_Config'], endpoint, patient_data_list)
            if converted_path:
                converted_files_paths.append(converted_path)
        
    return converted_files_paths

def process_claim(config, endpoint, patient_data_list):
    """
    Processes patient data for a specified endpoint, converting it into the 837P format.
    Generates a separate 837P file for each endpoint based on detailed patient data.

    Parameters:
    - config: Configuration settings loaded from a JSON file.
    - endpoint_key: The key representing the endpoint for which the data is being processed.
    - patient_data_list: A list of dictionaries, each containing detailed patient data.

    Returns:
    - Path to the converted file, or None if an error occurs.
    """
    # Retrieve endpoint-specific configuration
    endpoint_config = config['endpoints'].get(endpoint)
    if not endpoint_config:
        print("Endpoint configuration for {} not found.".format(endpoint))
        return None

    # Retrieve desired default output file path from config
    output_directory = config.get('outputFilePath', '')
    
    # BUG This is a WinSCP validation because of the mishandling of spaces in paths. 
    # This shouldn't need to exist.
    output_directory = winscp_validate_output_directory(output_directory)
    
    if not os.path.isdir(output_directory):
        print("Output directory does not exist. Please check the configuration.")
        return None

    # Initialize document segments with headers
    isa_header, gs_header = MediLink_837p_encoder_library.create_interchange_header(config, endpoint)
    document_segments = [isa_header, gs_header]

    # Initialize the transaction set control number
    transaction_set_control_number = 1

    # Process each patient's data in the list
    for patient_data in patient_data_list:
        # Assuming validate_claim_data is adapted to handle individual patient data dictionaries
        if True: #validate_claim_data(patient_data, config): BUG DISABLED VALIDATION
            # The format_single_claim function needs to be adapted to handle individual patient data dictionaries
            formatted_claim = format_single_claim(patient_data, config, endpoint, transaction_set_control_number)
            document_segments.append(formatted_claim)
            transaction_set_control_number += 1

    # Append interchange trailer
    ge_trailer, iea_trailer = MediLink_837p_encoder_library.create_interchange_trailer(config, endpoint, transaction_set_control_number - 1)
    document_segments.extend([ge_trailer, iea_trailer])

    # Write the complete 837P document to an output file and return its path
    return write_output_file(document_segments, output_directory, endpoint, patient_data_list[0]['file_path'], config)

# Validation Function checks the completeness and correctness of each claim's data
def validate_claim_data(parsed_data, config):
    required_fields = ['CHART', 'billing_provider_npi', 'IPOLICY', 'CODEA', 'DATE', 'AMOUNT', 'TOS', 'DIAG']
    errors = []

    # Check for missing or empty fields
    for field in required_fields:
        if not parsed_data.get(field):
            errors.append("Missing or empty field: {}".format(field))
    
    # Validate NPI format
    if not re.match(r'^\d{10}$', parsed_data.get('billing_provider_npi', '')):
        errors.append("Invalid NPI format: {}".format(parsed_data.get('billing_provider_npi')))

    # Validate date format
    try:
        datetime.strptime(parsed_data.get('DATE'), "%Y%m%d")
    except ValueError:
        errors.append("Invalid date format: {}".format(parsed_data.get('DATE')))

    # Log validation errors
    if errors:
        for error in errors:
            MediLink_837p_encoder_library.log(error, config, level="ERROR")
        return False
    
    return True

if __name__ == "__main__":
    """
    Converts fixed-width files to 837P format for health claim submissions.

    Usage:
    ------
    1. Convert a single file:
        python MediLink_837p_encoder.py -e [endpoint] -p [file_path]

    2. Convert all files in a directory:
        python MediLink_837p_encoder.py -e [endpoint] -p [directory_path] -d

    Arguments:
    ----------
    - "-e": Specify endpoint ("AVAILITY", "OPTUMEDI", "PNT_DATA").
    - "-p": Path to file/directory for processing.
    - "-d": Flag for directory processing.

    Note: Ensure correct config file path.
    """
    parser = argparse.ArgumentParser(
        description="Converts fixed-width files to the 837P format for health claim submissions. Supports processing individual files or all files within a directory.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-e", "--endpoint", 
        required=True,
        choices=["AVAILITY", "OPTUMEDI", "PNT_DATA"],
        help="Specify the endpoint for which the conversion is intended."
    )
    parser.add_argument(
        "-p", "--path", 
        required=True,
        help="Path to the input fixed-width file or directory to process. If a directory is provided, all .DAT files within will be processed."
    )
    parser.add_argument(
        "-d", "--is-directory", 
        action='store_true',
        help="Flag indicating the path provided is a directory. If set, all .DAT files within the directory will be processed."
    )
    args = parser.parse_args()

    print("Starting the conversion process for {}. Processing {} at '{}'.".format(args.endpoint, 'directory' if args.is_directory else 'file', args.path))

    # Load configuration
    config, _ = MediLink_ConfigLoader.load_configuration()
    
    def process_and_write_file(file_path, config, endpoint, starting_tscn=1):
        """
        Process a single file, create complete 837P document with headers and trailers, and write to output file.

        Parameters:
        - file_path: Path to the .DAT file to be processed.
        - config: Configuration settings.
        - endpoint: Endpoint key.
        - starting_tscn: Starting Transaction Set Control Number.
        """
        print("Processing: {}".format(file_path))
        formatted_data, transaction_set_control_number = process_file(file_path, config, endpoint, starting_tscn)
        isa_header, gs_header, ge_trailer, iea_trailer = create_interchange_elements(config, endpoint, transaction_set_control_number - 1)
        
        # Combine everything into a single document
        complete_document = "{}\n{}\n{}\n{}\n{}".format(
            isa_header,
            gs_header,
            formatted_data,
            ge_trailer,            
            iea_trailer
        )
        
        # Write to output file
        output_file_path = write_output_file([complete_document], config.get('outputFilePath', ''), endpoint, file_path, config)
        print("File processed. Output saved to: {}".format(output_file_path))
    
    if args.is_directory:
        # Process each .DAT file within the directory
        for file_name in os.listdir(args.path):
            if file_name.endswith(".DAT"):
                file_path = os.path.join(args.path, file_name)
                process_and_write_file(file_path, config, args.endpoint)
    else:
        # Process a single file
        process_and_write_file(args.path, config, args.endpoint)

    print("Conversion complete.")