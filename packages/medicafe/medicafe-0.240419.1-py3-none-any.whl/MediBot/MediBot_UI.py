from sys import exit
import ctypes
from ctypes import wintypes
import time
import re
import re  #for addresses
from MediBot_Preprocessor import config

"""
User Interaction Refinements
- [ ] Refine the menu options for clearer user guidance during script pauses and errors.
- [ ] Add functionality for user to easily repeat or skip specific entries without script restart.
    Develop more intuitive skip and retry mechanisms that are responsive to user input during data entry sessions.

"""
# Function to check if a specific key is pressed
VK_END = int(config.get('VK_END', ""), 16) # Try F12 (7B). Virtual key code for 'End' (23)
VK_PAUSE = int(config.get('VK_PAUSE', ""), 16) # Try F11 (7A). Virtual-key code for 'Home' (24)

MAPAT_MED_PATH = '' # Initialize global constant for MAPAT path
MEDISOFT_SHORTCUT = '' # Initialize global constant for LNK path

def is_key_pressed(key_code):
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    user32.GetAsyncKeyState.restype = wintypes.SHORT
    user32.GetAsyncKeyState.argtypes = [wintypes.INT]
    return user32.GetAsyncKeyState(key_code) & 0x8000 != 0

def manage_script_pause(csv_data, error_message, reverse_mapping):
    global script_paused
    #print("Debug - Entered manage_script_pause with pause status: {}".format(script_paused))
    user_action = 0 # initialize as 'continue'
    
    if not script_paused and is_key_pressed(VK_PAUSE):
        script_paused = True
        print("Script paused. Opening menu...")
        interaction_mode = 'normal'  # Assuming normal interaction mode for script pause
        user_action = user_interaction(csv_data, interaction_mode, error_message, reverse_mapping)
    
    while script_paused:
        if is_key_pressed(VK_END):
            script_paused = False
            print("Continuing...")
        elif is_key_pressed(VK_PAUSE):
            user_action = user_interaction(csv_data, 'normal', error_message, reverse_mapping)
        time.sleep(0.1)
    
    return user_action

# Menu Display & User Interaction
def display_patient_selection_menu(csv_data, reverse_mapping, proceed_as_medicare):
    selected_patient_ids = []
    selected_indices = []

    def display_menu_header(title):
        print("\n" + "-" * 60)
        print(title)
        print("-" * 60)

    def display_patient_list(csv_data, reverse_mapping, medicare_filter=False, exclude_medicare=False):
        medicare_policy_pattern = r"^[a-zA-Z0-9]{11}$"  # Regex pattern for 11 alpha-numeric characters
        primary_policy_number_header = reverse_mapping.get('Primary Policy Number', 'Primary Policy Number')
        primary_insurance_header = reverse_mapping.get('Primary Insurance', 'Primary Insurance')  # Adjust field name as needed
        
        displayed_indices = []
        displayed_patient_ids = []

        for index, row in enumerate(csv_data):
            policy_number = row.get(primary_policy_number_header, "")
            primary_insurance = row.get(primary_insurance_header, "").upper()
            
            if medicare_filter and (not re.match(medicare_policy_pattern, policy_number) or "MEDICARE" not in primary_insurance):
                continue
            if exclude_medicare and re.match(medicare_policy_pattern, policy_number) and "MEDICARE" in primary_insurance:
                continue

            patient_id_header = reverse_mapping['Patient ID #2']
            patient_name_header = reverse_mapping['Patient Name']
            patient_id = row.get(patient_id_header, "N/A")
            patient_name = row.get(patient_name_header, "Unknown")
            surgery_date = row.get('Surgery Date', "Unknown Date")  # Access 'Surgery Date' as string directly from the row
            
            print("{0:02d}: {3:.5s} (ID: {2}) {1} ".format(index+1, patient_name, patient_id, surgery_date))

            displayed_indices.append(index)
            displayed_patient_ids.append(patient_id)

        return displayed_indices, displayed_patient_ids

    if proceed_as_medicare:
        display_menu_header("MEDICARE Patient Selection for Today's Data Entry")
        selected_indices, selected_patient_ids = display_patient_list(csv_data, reverse_mapping, medicare_filter=True)
    else:
        display_menu_header("PRIVATE Patient Selection for Today's Data Entry")
        selected_indices, selected_patient_ids = display_patient_list(csv_data, reverse_mapping, exclude_medicare=True)

    print("-" * 60)
    proceed = input("\nDo you want to proceed with the selected patients? (yes/no): ").lower().strip() in ['yes', 'y']

    if not proceed:
        display_menu_header("Patient Selection for Today's Data Entry")
        selected_indices, selected_patient_ids = display_patient_list(csv_data, reverse_mapping)
        print("-" * 60)
        selection = input("\nEnter the number(s) of the patients you wish to proceed with \n(e.g., 1,3,5): ")
        selection = selection.replace('.', ',')  # Replace '.' with ',' in the user input just in case
        selected_indices = [int(x.strip()) - 1 for x in selection.split(',')]  
        proceed = True

    patient_id_header = reverse_mapping['Patient ID #2']
    selected_patient_ids = [csv_data[i][patient_id_header] for i in selected_indices if i < len(csv_data)]

    return proceed, selected_patient_ids, selected_indices

def display_menu_header(title):
    print("\n" + "-" * 60)
    print(title)
    print("-" * 60)

def handle_user_interaction(interaction_mode, error_message):
    while True:
        # If interaction_mode is neither 'triage' nor 'error', then it's normal mode.
        title = "Error Occurred" if interaction_mode == 'error' else "Data Entry Options"
        display_menu_header(title)

        if interaction_mode == 'error':
            print("\nERROR: ", error_message)

        # Need to tell the user which patient we're talking about because it won't be obvious anymore.
        # Also, this ERROR might be called from a location where the menu below isn't relevant like selecting patients 
        # -- need a better way to handle that.
        print("1: Retry last entry")
        print("2: Skip to next patient and continue")
        print("3: Go back two patients and redo")
        print("4: Exit script")
        print("-" * 60)
        choice = input("Enter your choice (1/2/3/4): ").strip()
        
        if choice == '1':
            print("Selected: 'Retry last entry'. Please press 'F12' to continue.")
            return -1
        elif choice == '2':
            print("Selected: 'Skip to next patient and continue'. Please press 'F12' to continue.")
            return 1
        elif choice == '3':
            print("Selected: 'Go back two patients and redo'. Please press 'F12' to continue.")
            # Returning a specific value to indicate the action of going back two patients
            # but we might run into a problem if we stop mid-run on the first row?
            return -2
        elif choice == '4':
            print("Exiting the script.")
            exit()
        else:
            print("Invalid choice. Please enter a valid number.")

def user_interaction(csv_data, interaction_mode, error_message, reverse_mapping):
    # Consider logging the actions taken during user interaction for audit purposes.
    global MAPAT_MED_PATH, MEDISOFT_SHORTCUT # Initialize global constants
    selected_patient_ids = []
    selected_indices = []

    if interaction_mode == 'triage':
    
        display_menu_header("            =(^.^)= Welcome to MediBot! =(^.^)=")
        
        while True:
            response = input("\nAm I processing Medicare patients? (yes/no): ").lower().strip()
            if response:  # Check if the response is not empty
                if response in ['yes', 'y']:
                    proceed_as_medicare = True
                    break
                elif response in ['no', 'n']:
                    proceed_as_medicare = False
                    break
                else:
                    print("Invalid entry. Please enter 'yes' or 'no'.")
            else:
                print("A response is required. Please try again.")

        MAPAT_MED_PATH = config.get('MEDICARE_MAPAT_MED_PATH', "") if proceed_as_medicare else config.get('MAPAT_MED_PATH', "")
        MEDISOFT_SHORTCUT = config.get('MEDICARE_SHORTCUT', "") if proceed_as_medicare else config.get('PRIVATE_SHORTCUT', "")
        
        fixed_values = config.get('fixed_values', {})  # Get fixed values from config json 
        if proceed_as_medicare:
            medicare_added_fixed_values = config.get('medicare_added_fixed_values', {})
            fixed_values.update(medicare_added_fixed_values) # Add any medicare-specific fixed values from config
        
        proceed, selected_patient_ids, selected_indices = display_patient_selection_menu(csv_data, reverse_mapping, proceed_as_medicare)
        return proceed, selected_patient_ids, selected_indices, fixed_values
    
    return handle_user_interaction(interaction_mode, error_message)