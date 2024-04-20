import os
import subprocess
import logging
import MediLink_837p_encoder
from MediLink_837p_encoder_library import log
from tqdm import tqdm
from MediLink_DataMgmt import operate_winscp

"""
Handles the transmission of files to endpoints and related tasks for the MediLink script.

Functions:
- check_internet_connection(): Checks for an active internet connection.
- UPDATE THIS: transmit_files_to_endpoint(converted_files, endpoint_config, local_storage_path): Transmits files to a specified endpoint using WinSCP.
- handle_transmission_result(transmission_result): Handles the result of the file transmission process.
- submit_claims(detailed_patient_data_grouped_by_endpoint, config): Submits claims to respective endpoints based on patient data and configuration.
- confirm_transmission(detailed_patient_data_grouped_by_endpoint): Displays patient data ready for transmission and asks for confirmation.

This module provides functionality for transmitting files, confirming transmissions, and ensuring connectivity for the MediLink script.
"""

# Internet Connectivity Check
def check_internet_connection():
    """
    Checks if there is an active internet connection.
    Returns: Boolean indicating internet connectivity status.
    """
    try:
        # Run a ping command to a reliable external server (e.g., Google's DNS server)
        ping_process = subprocess.Popen(["ping", "-n", "1", "8.8.8.8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ping_output, ping_error = ping_process.communicate()

        # Check if the ping was successful
        if "Reply from" in ping_output.decode("utf-8"):
            return True
        else:
            return False
    except Exception as e:
        print("An error occurred while checking internet connectivity:", e)
        return False
        
def handle_transmission_result(transmission_result):
    """
    Handles the result of the file transmission process. Logs the outcome and provides user feedback.

    :param transmission_result: The result of the file transmission process.
    """
    #if transmission_result:
        #logging.info("Transmission successful")
        # TODO This needs to do an actual check in the WinSCP log to make sure this is actually true.
        #print("Files have been successfully transmitted.")
    #else:
        #logging.error("Transmission failed")
        # TODO This needs to do a pull from the WinSCP log to show the user what happened.
        #print("There was an issue with the file transmission.")

def submit_claims(detailed_patient_data_grouped_by_endpoint, config):
    if not detailed_patient_data_grouped_by_endpoint:
        print("No new files detected for submission.")
        return

    # Wrap the iteration with tqdm for a progress bar
    for endpoint, patients_data in tqdm(detailed_patient_data_grouped_by_endpoint.items(), desc="Progress", unit="endpoint"):
        if not patients_data:  # Skip if no patient data for the endpoint
            continue

        # Confirm transmission to each endpoint with detailed overview
        if True: #confirm_transmission({endpoint: patients_data}):
            if check_internet_connection():
                # Process and transmit files per endpoint
                converted_files = MediLink_837p_encoder.convert_files_for_submission(patients_data, config)
                if converted_files:  # Check if files were successfully converted
                    # BUG DISABLE TRANSMISSION FOR TESTING
                    # transmission_result = operate_winscp("upload", converted_files, config['MediLink_Config']['endpoints'][endpoint], config['MediLink_Config']['local_claims_path'])
                    print("Would have uploaded here!") # DEBUG
                    
                    # handle_transmission_result(transmission_result)
                    # This doesn't really do much
                    # BUG This has to fail better. If one endpoint is unreachable, it should still try the next endpoint.
                    # BUG handle_transmission_result is wrong.
                else:
                    print("No files were converted for transmission to {0}.".format(endpoint))
            else:
                print("No internet connection detected.")
                try_again = input("Do you want to try again? (Y/N): ").strip().lower()
                if try_again != 'y':
                    print("Exiting transmission process. Please try again later.")
                    return  # Exiting the function if the user decides not to retry
        else:
            print("Transmission canceled for endpoint {0}.".format(endpoint))

    print("Claim submission completed.\n")

# Secure File Transmission
def confirm_transmission(detailed_patient_data_grouped_by_endpoint):
    """
    Displays detailed patient data ready for transmission and their endpoints, 
    asking for user confirmation before proceeding.

    :param detailed_patient_data_grouped_by_endpoint: Dictionary with endpoints as keys and 
            lists of detailed patient data as values.
    :param config: Configuration settings loaded from a JSON file.
    """ 
    print("\nReview of patient data ready for transmission:")
    for endpoint, patient_data_list in detailed_patient_data_grouped_by_endpoint.items():
        print("\nEndpoint: {0}".format(endpoint))
        for patient_data in patient_data_list:
            patient_info = "({1}) {0}".format(patient_data['patient_name'], patient_data['patient_id'])
            print("- {:<35} | {:<5}, ${:<6}, Primary: {}".format(
                patient_info, patient_data['surgery_date'][:5], patient_data['amount'], patient_data['primary_insurance']))
    
    confirmation = input("\nProceed with transmission to all endpoints? (Y/N): ").strip().lower()
    return confirmation == 'y'

# Entry point if this script is run directly. Probably needs to be handled better.
if __name__ == "__main__":
    print("Please run MediLink directly.")