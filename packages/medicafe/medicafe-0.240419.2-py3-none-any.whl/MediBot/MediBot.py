import subprocess
import os
import tempfile
import traceback
import re  #for addresses
from collections import OrderedDict
import MediBot_UI
import MediBot_dataformat_library
import MediBot_Preprocessor
from MediBot_Preprocessor import initialize, AHK_EXECUTABLE, CSV_FILE_PATH, field_mapping

# Add parent directory of the project to the Python path
import sys
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_dir)

from MediLink import MediLink_ConfigLoader

"""
# Development Task List for MediBot

Error Handling Improvements
- [ ] Develop a centralized error handling and logging mechanism for improved troubleshooting.
- [ ] Implement validation checks during patient data entry to prevent submission of incomplete or incorrect records.

Insurance Mode Adjustments
- [ ] Integrate a comprehensive list of insurance company codes for automatic selection.
- [ ] Automate insurance-specific data entry adjustments, such as character replacements specific to Medicare.

Diagnosis Entry
- [ ] Automate data extraction from Surgery Schedule to import to CSV a column indicating diagnosis code per px.

Script Efficiency and Reliability
- [ ] Ensure robust handling of Medisoft's field navigation quirks, particularly for fields that are skipped or require special access.

Documentation and Support
- [ ] Create detailed documentation for setup, configuration, and usage of the script.
- [ ] Establish a support channel for users to report issues or request features.

Future Directions
- [ ] Consider developing a graphical user interface (GUI) for non-technical users for easier script management and execution.

Medisoft Field Navigation: 
    Investigate and optimize navigation for fields that Medisoft skips or requires backward navigation to access.

Insurance Mode Features: 
    Evaluate the feasibility and implement the use of the F6 search for insurance address verification, enhancing user verification processes. 

Error Handling and Logging: 
    Implement a check for AHK script execution status, providing feedback or troubleshooting steps if the script encounters issues.
"""

def identify_field(header, field_mapping):
    for medisoft_field, patterns in field_mapping.items():
        for pattern in patterns:
            if re.search(pattern, header, re.IGNORECASE):
                return medisoft_field
    return None

    # Add this print to a function that is calling identify_field
    #print("Warning: No matching field found for CSV header '{}'".format(header))

# Function to execute an AutoHotkey script
def run_ahk_script(script_content):
    temp_script_name = None
    try:
        # Create a temporary AHK script file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.ahk') as temp_script:
            temp_script_name = temp_script.name
            temp_script.write(script_content.encode('utf-8'))
            temp_script.flush()
        # Attempt to run the AHK script
        subprocess.check_call([AHK_EXECUTABLE, temp_script_name])
    except subprocess.CalledProcessError as e:
        # This exception will catch any non-zero exit status from the AHK script
        print("AHK script failed with exit status:", e.returncode)
        print("Output from AHK script:", e.output)
    except Exception as e:
        # This catches any other exceptions that may occur
        print("An unexpected error occurred while running the AHK script:", e)
        traceback.print_exc()  # Print the stack trace of the exception
    finally:
        # Delete the temporary script file
        if temp_script_name:
            try:
                os.unlink(temp_script_name)
            except OSError as e:
                print("Error deleting temporary script file:", e)

# Global variable to store the last processed entry
last_processed_entry = None
# Global variable to store temporarily parsed address components
parsed_address_components = {}

def process_field(medisoft_field, csv_row, parsed_address_components, reverse_mapping, csv_data, fixed_values):
    global last_processed_entry
    
    try:
        value = ''
        if medisoft_field in parsed_address_components:
            value = parsed_address_components.get(medisoft_field, '')
        elif medisoft_field in fixed_values:
            value = fixed_values[medisoft_field][0]  # Use the fixed value
        elif medisoft_field in reverse_mapping:
            csv_header = reverse_mapping[medisoft_field]
            value = csv_row.get(csv_header, '')

        formatted_value = MediBot_dataformat_library.format_data(medisoft_field, value, csv_data, reverse_mapping, parsed_address_components) if value else 'Send, {Enter}'
        run_ahk_script(formatted_value)

        last_processed_entry = (medisoft_field, value)
        return 'continue', last_processed_entry
    except Exception as e:
        return handle_error(e, medisoft_field, last_processed_entry, csv_data)

def handle_error(error, medisoft_field, last_processed_entry, csv_data):
    print("An error occurred while processing {0}: {1}".format(medisoft_field, error))
    # Assuming the interaction mode is 'error' in this case
    interaction_mode = 'error'
    response = MediBot_UI.user_interaction(csv_data, interaction_mode, error, reverse_mapping)
    return response, last_processed_entry

# iterating through each field defined in the field_mapping.
def iterate_fields(csv_row, field_mapping, parsed_address_components, reverse_mapping, csv_data, fixed_values):
    global last_processed_entry
    # Check for user action at the start of each field processing
    for medisoft_field in field_mapping.keys():
        action = MediBot_UI.manage_script_pause(csv_data,'',reverse_mapping) # per-field pause availability. Necessary to provide frequent opportunities for the user to pause the script.
        if action != 0:  # If action is either 'Retry' (-1) or 'Skip' (1)
            return action  # Break out and pass the action up
        
        # Process each field in the row
        _, last_processed_entry = process_field(medisoft_field, csv_row, parsed_address_components, reverse_mapping, csv_data, fixed_values)
        
    return 0 # Default action to continue

def data_entry_loop(csv_data, field_mapping, reverse_mapping, fixed_values):
    global last_processed_entry, parsed_address_components, script_paused
    script_paused = False
    error_message = ''  # Initialize error_message once
    current_row_index = 0

    while current_row_index < len(csv_data):
        row = csv_data[current_row_index]
        
        # Handle script pause at the start of each row (patient record). 
        MediBot_UI.manage_script_pause(csv_data, error_message, reverse_mapping)
        error_message = ''  # Clear error message for the next iteration
        
        if script_paused:
            continue  # Skip processing this row if the script is paused

        # I feel like this is overwriting what would have already been idenfitied in the mapping. 
        # This probably needs to be initialized differently.
        # parsed_address_components = {'City': '', 'State': '', 'Zip Code': ''}
        parsed_address_components = {}

        # Process each field in the row
        action = iterate_fields(row, field_mapping, parsed_address_components, reverse_mapping, csv_data, fixed_values)
        # TODO add a feature here where if you accidentally started overwriting a patient that you could go back 2 patients.
        # Need to tell the user which patient we're talking about because it won't be obvious anymore.
        if action == -1:  # Retry
            continue  # Remain on the current row. 
        elif action == 1:  # Skip
            if current_row_index == len(csv_data) - 1:  # If it's the last row
                print("Reached the end of the patient list. Looping back to the beginning.")
                current_row_index = 0  # Reset to the first row
            else:
                current_row_index += 1 # Move to the next row
            continue
        elif action == -2:  # Go back two patients and redo
            current_row_index = max(0, current_row_index - 2)  # Go back two rows, but not below 0
            continue

        # Code to handle the end of a patient record
        # print("\nA patient record was completed.")
        script_paused = True
        # Handle script pause at the end of each row (patient record).
        current_row_index += 1  # Move to the next row by default

def open_medisoft(shortcut_path):
    try:
        os.startfile(shortcut_path)
        print("Medisoft is being opened...\n")
    except subprocess.CalledProcessError as e:
        print("Failed to open Medisoft:", e)
        print("Please manually open Medisoft.")
    except Exception as e:
        print("An unexpected error occurred:", e)
        print("Please manually open Medisoft.")
    finally:
        print("Press 'F12' to begin data entry.")

# Placeholder for any cleanup
def cleanup():
    print("\n**** Medibot Finished! ****\n")
    # THis might need to delete the staging stuff that gets set up by mostly MediLink but maybe other stuff too.
    pass 

class ExecutionState:
    def __init__(self) -> None:
        
        #print("Loading Configuration...")
        config, _ = MediLink_ConfigLoader.load_configuration(config_path, crosswalk_path)
        
        self.verify_config_type(config)
        #print("Initializing Constants...")
        initialize(config)
        
    def verify_config_type(self, config):
        if not isinstance(config, (dict, OrderedDict)):
            raise TypeError("Error: Configuration must be a dictionary or an OrderedDict. Check unpacking.")

# Main script execution wrapped in try-except for error handling
if __name__ == "__main__":
    e_state = None
    try:
# Default paths
        default_config_path = os.path.join(os.path.dirname(__file__), '..', 'json', 'config.json')
        default_crosswalk_path = os.path.join(os.path.dirname(__file__), '..', 'json', 'crosswalk.json')

        # Check if command-line arguments are provided
        if len(sys.argv) > 1:
            # If arguments are provided, use them
            config_path = sys.argv[1]
            crosswalk_path = sys.argv[2] if len(sys.argv) > 2 else default_crosswalk_path
        else:
            # If no arguments are provided, use default paths
            config_path = default_config_path
            crosswalk_path = default_crosswalk_path
        
        e_state = ExecutionState()
        
        #print("Loading CSV Data...")
        csv_data = MediBot_Preprocessor.load_csv_data(CSV_FILE_PATH)
        
        #print("Pre-processing CSV Data...")
        MediBot_Preprocessor.preprocess_csv_data(csv_data)  # Pre-process CSV data to add combined fields
        headers = csv_data[0].keys() # Including Patient Name and Patient Address
        
        #print("Performing Intake Scan...")
        # identified_fields is an OrderedDict
        identified_fields = MediBot_Preprocessor.intake_scan(headers, field_mapping)
        
        # Reverse the identified_fields mapping for lookup
        reverse_mapping = {v: k for k, v in identified_fields.items()}

        # CSV Patient Triage
        interaction_mode = 'triage'  # Start in triage mode
        error_message = ""  # This will be filled if an error has occurred
        #print("Debug - Identified fields mapping (main): {}".format(identified_fields)) # Debug Line
        
        proceed, selected_patient_ids, selected_indices, fixed_values = MediBot_UI.user_interaction(csv_data, interaction_mode, error_message, reverse_mapping)

        if proceed:
            # Filter csv_data for selected patients from Triage mode.
            csv_data = [row for index, row in enumerate(csv_data) if index in selected_indices]
            existing_patients, patients_to_process = MediBot_Preprocessor.check_existing_patients(selected_patient_ids, MediBot_UI.MAPAT_MED_PATH)
            
            if existing_patients:
                print("\nNOTE: The following patient(s) already EXIST in the system and \nwill be excluded from processing:")
                for patient_id, patient_name in existing_patients:
                    print("(ID: {0}) {1}".format(patient_id, patient_name))
                # Update csv_data to exclude existing patients
                csv_data = [row for row in csv_data if row[reverse_mapping['Patient ID #2']] in patients_to_process]
            else:
                print("\nSelected patient(s) are NEW patients and will be processed.")

            if len(patients_to_process) == 0:
                proceed = input("\nAll patients have been processed. Continue anyway?: ").lower().strip() in ['yes', 'y']
            else:
                proceed = input("\nDo you want to proceed with the {} remaining patient(s)? (yes/no): ".format(len(patients_to_process))).lower().strip() in ['yes', 'y']

            if proceed:
            
            #    Would be nice to have some kind of self-test here.
            #    print("\nDebug - Starting AHK script. Reload AHK if failed...")
            #    try:
            #        subprocess.call([AHK_EXECUTABLE, r"G:\My Drive\CocoWave\XP typing bot\notepad_test.ahk"])
            #        run_ahk_script('MsgBox, Test AHK Script Execution')
            #    except subprocess.CalledProcessError as e:
            #        print("Error running AHK script. Please reload AHK and try again. Error: {}".format(e))
            #        exit(1)
            #    except Exception as e:
            #        print("An unexpected error occurred while running the AHK script: {}".format(e))
            #        exit(1)

                print("\nRemember, when in Medisoft:")
                print("  Press 'F8'  to create a New Patient.")
                print("  Press 'F12' to begin data entry.")
                print("  Press 'F11' at any time to Pause.")
                input("\n*** Press [Enter] when ready to begin! ***\n")
                open_medisoft(MediBot_UI.MEDISOFT_SHORTCUT)
                script_paused = True
                _ = MediBot_UI.manage_script_pause(csv_data, error_message, reverse_mapping)
                data_entry_loop(csv_data, field_mapping, reverse_mapping, fixed_values)
                cleanup()                
            else:
                print("Data entry canceled by user.")
    except Exception as e:
        if e_state:
            interaction_mode = 'error'  # Switch to error mode
            error_message = str(e)  # Capture the error message
        print("An error occurred: {0}".format(e))
        # Handle the error by calling user interaction with the error information
        # Ensure that identified_fields is defined before using it in user interaction
        if 'identified_fields' in locals():
            _ = MediBot_UI.user_interaction(csv_data, interaction_mode, error_message, reverse_mapping)
        else:
            print("Please ensure CSV headers match expected field names in config file, then re-run Medibot.")

# Performance: Process flow (25px - 13 min)
# 2:00 Internet connect & Email 
# 6:00 6 px medicare
# 1:00 menu handling for privado
# 4:00 5 px privado