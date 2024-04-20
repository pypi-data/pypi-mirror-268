import os
import MediLink_ConfigLoader
import MediLink_837p_encoder
import logging
import MediLink_Down
import MediLink_Up

# For UI Functions
import os
import MediLink_UI  # Import UI module for handling all user interfaces

"""
Development Tasks for Backend Enhancement in MediSoft Claims Submittal (MediLink) Script:

Implement dynamic configurations for multiple endpoints (Availity, Optum, PNT Data) with environmental settings support.
Enhance file detection with detailed logging and introduce integrity checks for pre-processing validation.
Verify file transmissions via WinSCP log analysis for successful endpoint acknowledgments and secure data transfer.
Automate response file handling from endpoints and integrate feedback into MediSoft with exception alerts.
De-persisting Intermediate Files.
When transmissions fail, there is some retaining of patient data in memory or something that seems to default
any new endpoint changes to Optum. May need to "de-confirm" patients, but leave the suggested endpoints as the previously
confirmed endpoints. This should be similar logic to if the user made a mistake and wants to go back and fix it.
These tasks involve backend enhancements such as dynamic configurations, file detection improvements, file transmission verification, automation of response file handling, and management of intermediate files and transmission failures.

TODO Crosswalk should be to PayerID key vs Medisoft:Endpoint.
TODO Availity has a response file that says "File was received at TIME. File was sent for processing." as a confirmation 
that sits in the SendFiles folder after a submittal. 

BUG Suggested Endpoint when you say 'n' to proceed with transmission is not getting updated with the endpoint 
that was selected previously by the user. However, when we go back to the confirmation list, we do have a persist of the assignment.
This can be confusing for the user.
"""

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s\n')

def detect_and_display_file_summaries(directory_path, config, crosswalk):
    """
    Detects new files in the specified directory and prepares detailed patient data for processing,
    including suggestions for endpoints based on insurance provider information found in the config.
    
    :param directory_path: Path to the directory containing files to be detected.
    :param config: Configuration settings loaded from a JSON file.
    :return: A tuple containing a list of new file paths and the detailed patient data.
    """
    new_files = detect_new_files(directory_path)
    if not new_files:
        print("    No new claims detected. Check Medisoft claims output.\n")
        return False, []

    detailed_patient_data = []  # Initialize list for detailed patient data
    for file_path in new_files:
        detailed_data = extract_and_suggest_endpoint(file_path, config, crosswalk)
        detailed_patient_data.extend(detailed_data)  # Accumulate detailed data for processing

    # Return just the list of new files and the enriched detailed patient data
    return new_files, detailed_patient_data

def detect_new_files(directory_path, file_extension='.DAT'):
    """
    Scans the specified directory for new files with a given extension.
    
    :param directory_path: Path to the directory containing files to be detected.
    :param file_extension: Extension of the files to detect. Defaults to '.csv'.
    :return: A list of paths to new files detected in the directory.
    """
    detected_file_paths = []
    for filename in os.listdir(directory_path):
        if filename.endswith(file_extension):
            file_path = os.path.join(directory_path, filename)
            detected_file_paths.append(file_path)
    return detected_file_paths

def extract_and_suggest_endpoint(file_path, config, crosswalk):
    """
    Reads a fixed-width file, extracts file details including surgery date, patient ID, 
    patient name, primary insurance, and other necessary details for each record. It suggests 
    an endpoint based on insurance provider information found in the crosswalk and prepares 
    detailed patient data for processing.
    
    Parameters:
    - file_path: Path to the fixed-width file.
    - crosswalk: Crosswalk dictionary loaded from a JSON file.

    Returns:
    - A comprehensive data structure retaining detailed patient claim details needed for processing,
      including new key-value pairs for file path, surgery date, patient name, and primary insurance.
    """
    detailed_patient_data = []
    
    for personal_info, insurance_info, service_info in MediLink_837p_encoder.read_fixed_width_data(file_path, config.get('MediLink_Config', {})):
        parsed_data = MediLink_837p_encoder.parse_fixed_width_data(personal_info, insurance_info, service_info, config.get('MediLink_Config', {}))
        
        primary_insurance = parsed_data.get('INAME')
        
        # TODO This suggested endpoint should be a payerid_to_endpoint_mapping.
        suggested_endpoint = crosswalk['insurance_to_endpoint_mapping'].get(primary_insurance, 'AVAILITY')
        
        # Directly enrich detailed patient data with additional information and suggested endpoint
        detailed_data = parsed_data.copy()  # Copy parsed_data to avoid modifying the original dictionary
        detailed_data.update({
            'file_path': file_path,
            'patient_id': parsed_data.get('CHART'),
            'surgery_date': parsed_data.get('DATE'),
            'patient_name': ' '.join([parsed_data.get(key, '') for key in ['FIRST', 'MIDDLE', 'LAST']]),
            'amount': parsed_data.get('AMOUNT'),
            'primary_insurance': primary_insurance,
            'suggested_endpoint': suggested_endpoint
        })
        detailed_patient_data.append(detailed_data)

    # Return only the enriched detailed patient data, eliminating the need for a separate summary list
    return detailed_patient_data

def organize_patient_data_by_endpoint(detailed_patient_data):
    """
    Organizes detailed patient data by their confirmed endpoints.
    This simplifies processing and conversion per endpoint basis, ensuring that claims are generated and submitted
    according to the endpoint-specific requirements.

    :param detailed_patient_data: A list of dictionaries, each containing detailed patient data including confirmed endpoint.
    :return: A dictionary with endpoints as keys and lists of detailed patient data as values for processing.
    """
    organized = {}
    for data in detailed_patient_data:
        # Retrieve confirmed endpoint from each patient's data
        endpoint = data['confirmed_endpoint'] if 'confirmed_endpoint' in data else data['suggested_endpoint']
        # Initialize a list for the endpoint if it doesn't exist
        if endpoint not in organized:
            organized[endpoint] = []
        organized[endpoint].append(data)
    return organized

def check_for_new_remittances(config):
    print("\nChecking for new files across all endpoints...")
    endpoints = config['MediLink_Config']['endpoints']
    for endpoint_key, endpoint_info in endpoints.items():
        try:
            # Pass the endpoint key to MediLink_Down.main() as an argument
            ERA_path = MediLink_Down.main(desired_endpoint=endpoint_key)
            # BUG This needs to check to see if this actually worked maybe winscplog before saying it completed successfully 
            print("New remittances for {} completed successfully.".format(endpoint_info['name']))
            print("Results saved to: {}\n".format(ERA_path))
        except Exception as e:
            print("An error occurred while checking remittances for {}: {}".format(endpoint_info['name'], e))

def user_decision_on_suggestions(detailed_patient_data, config):
    """
    Presents the user with all patient summaries and suggested endpoints,
    then asks for confirmation to proceed with all or specify adjustments manually.
    """
    # Display summaries of patient details and endpoints.
    MediLink_UI.display_patient_summaries(detailed_patient_data)

    # Ask the user if they want to proceed with all suggested endpoints.
    proceed = MediLink_UI.ask_for_proceeding_with_endpoints()

    # If the user agrees to proceed with all suggested endpoints, confirm them.
    if proceed:
        return confirm_all_suggested_endpoints(detailed_patient_data)
    # Otherwise, allow the user to adjust the endpoints manually.
    else:
        return select_and_adjust_files(detailed_patient_data, config)
    
def confirm_all_suggested_endpoints(detailed_patient_data):
    """
    Confirms all suggested endpoints for each patient's detailed data.
    """
    for data in detailed_patient_data:
        if 'confirmed_endpoint' not in data:
            data['confirmed_endpoint'] = data['suggested_endpoint']
    return detailed_patient_data

def select_and_adjust_files(detailed_patient_data, config):
    """
    Allows users to select patients and adjust their endpoints by interfacing with UI functions.
    """
    # Display options for patients
    MediLink_UI.display_patient_options(detailed_patient_data)

    # Get user-selected indices for adjustment
    selected_indices = MediLink_UI.get_selected_indices(len(detailed_patient_data))

    # Fetch endpoint names dynamically from the JSON config
    endpoint_mapping = {str(i + 1): config['MediLink_Config']['endpoints'][endpoint]['name'] for i, endpoint in enumerate(config['MediLink_Config']['endpoints'])}

    # Iterate over each selected index and process endpoint changes
    for i in selected_indices:
        data = detailed_patient_data[i]
        MediLink_UI.display_patient_for_adjustment(data['patient_name'], data.get('suggested_endpoint', 'N/A'))
        
        endpoint_change = MediLink_UI.get_endpoint_decision()

        if endpoint_change == 'y':
            MediLink_UI.display_endpoint_options(endpoint_mapping)            
            new_endpoint_choice = MediLink_UI.get_new_endpoint_choice()
            
            if new_endpoint_choice in endpoint_mapping:
                data['confirmed_endpoint'] = endpoint_mapping[new_endpoint_choice]
                print("Endpoint changed to {0} for patient {1}.".format(data['confirmed_endpoint'], data['patient_name']))
            else:
                print("Invalid selection. Keeping the suggested endpoint.")
        else:
            data['confirmed_endpoint'] = data.get('suggested_endpoint', 'N/A')

    # Return the updated data
    return detailed_patient_data

def main_menu():
    """
    Initializes the main menu loop and handles the overall program flow,
    including loading configurations and managing user input for menu selections.
    """
    # Load configuration settings and display the initial welcome message.
    config, crosswalk = MediLink_ConfigLoader.load_configuration() # BUG does this need an argument?
    
    # Display Welcome Message
    MediLink_UI.display_welcome()

    # Normalize the directory path for file operations.
    directory_path = os.path.normpath(config['MediLink_Config']['inputFilePath'])

    # Detect new files and collect detailed patient data if available.
    new_files, detailed_patient_data = detect_and_display_file_summaries(directory_path, config, crosswalk)

    while True:
        # Define the menu options. Base options include checking remittances and exiting the program.
        options = ["Check for new remittances", "Exit"]
        # If new files are detected, add the option to submit claims.
        if new_files:
            options.insert(1, "Submit claims")

        # Display the dynamically adjusted menu options.
        MediLink_UI.display_menu(options)
        # Retrieve user choice and handle it.
        choice = MediLink_UI.get_user_choice()

        if choice == '1':
            # Handle remittance checking.
            check_for_new_remittances(config)
        elif choice == '2' and new_files:
            # Handle the claims submission flow if new files are present.
            handle_submission(detailed_patient_data, config)
        elif choice == '3' or (choice == '2' and not new_files):
            # Exit the program if the user chooses to exit or if no new files are present.
            MediLink_UI.display_exit_message()
            break
        else:
            # Display an error message if the user's choice does not match any valid option.
            MediLink_UI.display_invalid_choice()

def handle_submission(detailed_patient_data, config):
    """
    Handles the submission process for claims based on detailed patient data.
    This function orchestrates the flow from user decision on endpoint suggestions to the actual submission of claims.
    """
    # Initiate user interaction to confirm or adjust suggested endpoints.
    adjusted_data = user_decision_on_suggestions(detailed_patient_data, config)
    # Confirm all remaining suggested endpoints.
    confirmed_data = confirm_all_suggested_endpoints(adjusted_data)
    if confirmed_data:  # Proceed if there are confirmed data entries.
        # Organize data by confirmed endpoints for submission.
        organized_data = organize_patient_data_by_endpoint(confirmed_data)
        # Confirm transmission with the user and check for internet connectivity.
        if MediLink_Up.confirm_transmission(organized_data):
            if MediLink_Up.check_internet_connection():
                # Submit claims if internet connectivity is confirmed.
                MediLink_Up.submit_claims(organized_data, config)
            else:
                # Notify the user of an internet connection error.
                print("Internet connection error. Please ensure you're connected and try again.")
        else:
            # Notify the user if the submission is cancelled.
            print("Submission cancelled. No changes were made.")

if __name__ == "__main__":
    main_menu()