import csv
import subprocess
import os
import re
from datetime import datetime
from collections import OrderedDict # so that the field_mapping stays in order.
import re
import sys

# Add parent directory of the project to the Python path
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_dir)

from MediLink import MediLink_ConfigLoader
from MediLink import MediLink_DataMgmt

"""
Preprocessing Enhancements
- [X] Preprocess Insurance Policy Numbers and Group Numbers to replace '-' with ''.
- [X] De-duplicate entries in the CSV and only entering the px once even if they show up twice in the file.
- [ ] Implement dynamic field combination in CSV pre-processing for flexibility with various CSV formats.
- [ ] Enhance SSN cleaning logic to handle more variations of sensitive data masking.
- [ ] Optimize script startup and CSV loading to reduce initial latency.

Data Integrity and Validation
- [ ] Conduct a thorough CSV integrity check before processing to flag potential issues upfront.
- [ ] Implement a mechanism to confirm the accuracy of entered data, potentially through a verification step or summary report.
- [ ] Explore the possibility of integrating direct database queries for existing patient checks to streamline the process.
- [ ] Automate the replacement of spaces with underscores ('_') in last names for Medicare entries, ensuring data consistency.
- [ ] Enhance CSV integrity checks to identify and report potential issues with data format, especially concerning insurance policy numbers and special character handling.

Known Issues and Bugs
- [ ] Address the handling of '.' and other special characters that may disrupt parsing, especially under Windows XP.
- [ ] Investigate the issue with Excel modifying long policy numbers in the CSV and provide guidance or a workaround.

Future Work
- [ ] Consolidate data from multiple sources (Provider_Notes.csv, Surgery_Schedule.csv, and Carols_CSV.csv) into a single table with Patient ID as the key, ensuring all data elements are aligned and duplicate entries are minimized.
- [ ] Implement logic to verify and match Patient IDs across different files to ensure data integrity before consolidation.
- [ ] Optimize the preprocessing of surgery dates and diagnosis codes for use in patient billing and scheduling systems.
- [ ] This needs to be able to take in the Surgery Schedule doc and parse out a Patient ID : Diagnosis Code table
- [ ] The Minutes & Cacncellation data with logic to consolidate into one table in memory.


Future Work: crosswalk_update() automates the process of updating the crosswalk.json file with new Medisoft insurance information.

Development Roadmap:
1. Problem Statement:
    - The need to update the crosswalk.json file arises whenever a new Medisoft insurance is discovered. Automation of this process is required for accuracy and efficiency.

2. Identifying New Insurance:
    - New Medisoft insurances are identified based on the payer ID number.
    - The existence of the payer ID number is checked in the crosswalk.json under existing endpoints.

3. Adding New Insurance:
    - If the payer ID number does not exist in any endpoint, the tool prompts the user, assisted by endpoint APIs, to add the payer ID to a specific endpoint.
    - The corresponding name from Carol's spreadsheet is used as the value for the new payer ID.

4. Mapping to Main Insurance:
    - The tool presents the user with a list of the top 5-7 insurances, scored higher on a fuzzy search or above a certain score.
    - The user selects the appropriate insurance based on the identified Medisoft insurance, establishing the medisoft_insurance_to_payer_id relationship.

5. Confirming Mapping:
    - The tool implicitly establishes the insurance_to_endpoint_mapping based on the selected MediSoft name and endpoint.
    - This step is confirmed or re-evaluated to ensure accuracy.

6. User Interaction:
    - Unrecognized payer IDs are presented to the user.
    - Users can assign these payer IDs to MediSoft custom names individually.
    - Grouping of payer IDs may be facilitated, especially for insurances like CIGNA with multiple addresses but few payer IDs.

7. Handling Unavailable Payer IDs:
    - An extra endpoint named "Fax/Mail or Other" is created to handle cases where the payer ID is unavailable.
    - The tool retains payer IDs not existing in any endpoint, allowing users to assign them to the "Fax/Mail or Other" key in the crosswalk.

8. Implementation Considerations:
    - The tool should handle various scenarios, including checking for free payer IDs and determining the appropriate endpoint for assignment.
    - Integration of API checks to verify payer ID availability and associated information is recommended.
    - Validation mechanisms should be implemented to prevent incorrect mappings and ensure data integrity.

NOTE: this needs to also pull from the CSV the listed address of the insruance.
NOTE: La Forma Z can have the PatientID number which can link back to Carol's table which can then map the Medisoft insurance name to the payerID 
and payer name and address when the insurance is already selected in Medisoft so the program can learn retroactively and would know the Medisoft # from
the sequencing rather than trying to feed it from the beginning. so that'll be out of ["fixedWidthSlices"]["personal_slices"]["PATID"].
NOTE: Also check MAPAT because maybe the PatientID to Medisoft custom insurance name might exist there enmasse + the PatientID to PayerID link from Carol's CSV
gives us the Medisoft custom insurance name to Payer ID. Then, the endpoint mapping is the clearinghouse PayerID list (API?). MAPAT has the PatientID to Medisoft 
insruance reference number which is the MAINS offset by 1 for the header. MAPAT has columns [159,162] for insurance and [195,200] for patient ID.
"""

# Load configuration
# Should this also take args? Path for ./MediLink needed to be added for this to resolve
config, _ = MediLink_ConfigLoader.load_configuration()

class InitializationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def initialize(config):
    global AHK_EXECUTABLE, CSV_FILE_PATH, field_mapping, page_end_markers
    
    try:
        AHK_EXECUTABLE = config.get('AHK_EXECUTABLE', "")
    except AttributeError:
        raise InitializationError("Error: 'AHK_EXECUTABLE' not found in config.")
    
    try:
        CSV_FILE_PATH = config.get('CSV_FILE_PATH', "")
    except AttributeError:
        raise InitializationError("Error: 'CSV_FILE_PATH' not found in config.")
    
    try:
        field_mapping = OrderedDict(config.get('field_mapping', {}))
    except AttributeError:
        raise InitializationError("Error: 'field_mapping' not found in config.")
    
    try:
        page_end_markers = config.get('page_end_markers', [])
    except AttributeError:
        raise InitializationError("Error: 'page_end_markers' not found in config.")


def open_csv_for_editing(csv_file_path):
    try:
        # Open the CSV file in the default program
        subprocess.run(['open' if os.name == 'posix' else 'start', csv_file_path], check=True, shell=True)
        print("After saving the revised CSV, please re-run MediBot.")
    except subprocess.CalledProcessError as e:
        print("Failed to open CSV file:", e)
        
# Function to load and process CSV data
def load_csv_data(csv_file_path):
    try:
        # Check if the file exists
        if not os.path.exists(csv_file_path):
            raise FileNotFoundError("***Error: CSV file '{}' not found.".format(csv_file_path))
        
        with open(csv_file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]  # Return a list of dictionaries
    except FileNotFoundError as e:
        print(e)  # Print the informative error message
        print("Hint: Check if CSV file is located in the expected directory or specify a different path in config file.")
        print("Please correct the issue and re-run MediBot.")
        sys.exit(1)  # Halt the script
    except IOError as e:
        print("Error reading CSV file: {}. Please check the file path and permissions.".format(e))
        sys.exit(1)  # Halt the script in case of other IO errors

# CSV Preprocessor built for Carol
def preprocess_csv_data(csv_data):
    try:
        # Filter out rows without a Patient ID
        csv_data[:] = [row for row in csv_data if row.get('Patient ID', '').strip()]
        
        # Remove Patients (rows) that are Primary Insurance: 'AETNA', 'AETNA MEDICARE', or 'HUMANA MED HMO'.
        csv_data[:] = [row for row in csv_data if row.get('Primary Insurance', '').strip() not in ['AETNA', 'AETNA MEDICARE', 'HUMANA MED HMO']]
                
        # Convert 'Surgery Date' to datetime objects for sorting
        for row in csv_data:
            try:
                row['Surgery Date'] = datetime.strptime(row.get('Surgery Date', ''), '%m/%d/%Y')
            except ValueError:
                # Handle or log the error if the date is invalid
                row['Surgery Date'] = datetime.min  # Assign a minimum datetime value for sorting purposes

        # Initially sort the patients first by 'Surgery Date' and then by 'Patient Last' alphabetically
        csv_data.sort(key=lambda x: (x['Surgery Date'], x.get('Patient Last', '').strip()))
        
        # Deduplicate patient records based on Patient ID, keeping the entry with the earliest surgery date
        unique_patients = {}
        for row in csv_data:
            patient_id = row.get('Patient ID')
            if patient_id not in unique_patients or row['Surgery Date'] < unique_patients[patient_id]['Surgery Date']:
                unique_patients[patient_id] = row
        
        # Update csv_data to only include unique patient records
        csv_data[:] = list(unique_patients.values())

        # Re-sort the csv_data after deduplication to ensure correct order
        csv_data.sort(key=lambda x: (x['Surgery Date'], x.get('Patient Last', '').strip()))
        
        # Maybe make a dataformat_library function for this? csv_data = format_preprocessor(csv_data)?
        for row in csv_data:
            # Convert 'Surgery Date' back to string format if needed for further processing (cleanup)
            row['Surgery Date'] = row['Surgery Date'].strftime('%m/%d/%Y')
            
            # Combine name fields
            first_name = row.get('Patient First', '').strip()
            middle_name = row.get('Patient Middle', '').strip()
            last_name = row.get('Patient Last', '').strip()
            row['Patient Name'] = "{}, {} {}".format(last_name, first_name, middle_name).strip()

            # Combine address fields
            address1 = row.get('Patient Address1', '').strip()
            address2 = row.get('Patient Address2', '').strip()
            row['Patient Street'] = "{} {}".format(address1, address2).strip()
            
            # Probably make a data_format function for this:
            # Define the replacements as a dictionary
            replacements = {
                '777777777': '',  # Replace '777777777' with an empty string
                'RAILROAD MEDICARE': 'RAILROAD',  # Replace 'RAILROAD MEDICARE' with 'RAILROAD'
                'AARP MEDICARE COMPLETE': 'AARP COMPLETE'  # Replace 'AARP MEDICARE COMPLETE' with 'AARP COMPLETE'
            }

            # Iterate over each key-value pair in the replacements dictionary
            for old_value, new_value in replacements.items():
                # Replace the old value with the new value if it exists in the row
                if row.get('Patient SSN', '') == old_value:
                    row['Patient SSN'] = new_value
                elif row.get('Primary Insurance', '') == old_value:
                    row['Primary Insurance'] = new_value

    except Exception as e:
        print("An error occurred while pre-processing CSV data. Please repair the CSV directly and try again:", e)

def check_existing_patients(selected_patient_ids, MAPAT_MED_PATH):
    existing_patients = []
    patients_to_process = list(selected_patient_ids)  # Clone the selected patient IDs list

    try:
        with open(MAPAT_MED_PATH, 'r') as file:
            next(file)  # Skip header row
            for line in file:
                if line.startswith("0"): # 1 is a flag for a deleted record so it would need to be re-entered.
                    patient_id = line[194:202].strip()  # Extract Patient ID (Columns 195-202)
                    patient_name = line[9:39].strip()  # Extract Patient Name (Columns 10-39)
                    
                    if patient_id in selected_patient_ids:
                        existing_patients.append((patient_id, patient_name))
                        # Remove all occurrences of this patient_id from patients_to_process as a filter rather than .remove because 
                        # then it only makes one pass and removes the first instance.
    except FileNotFoundError:
        # Handle the case where MAPAT_MED_PATH is not found
        print("MAPAT.med was not found at location indicated in config file.")
        print("Skipping existing patient check and continuing...")
        
    # Filter out all instances of existing patient IDs
    patients_to_process = [id for id in patients_to_process if id not in [patient[0] for patient in existing_patients]]
    
    return existing_patients, patients_to_process

def intake_scan(csv_headers, field_mapping):
    identified_fields = OrderedDict()
    missing_fields_warnings = []
    required_fields = config["required_fields"]
    
    # Iterate over the Medisoft fields defined in field_mapping
    for medisoft_field in field_mapping.keys():
        for pattern in field_mapping[medisoft_field]:
            matched_headers = [header for header in csv_headers if re.search(pattern, header, re.IGNORECASE)]
            if matched_headers:
                # Assuming the first matched header is the desired one
                identified_fields[matched_headers[0]] = medisoft_field
                break
        else:
            # Check if the missing field is a required field before appending the warning
            if medisoft_field in required_fields:
                missing_fields_warnings.append("WARNING: No matching CSV header found for Medisoft field '{0}'".format(medisoft_field))
   
   #-----------------------
   # CSV Integrity Check
   #-----------------------
   
   # This section needs to be revamped further so that it can interpret the information from here and decide 
   # if it's significant or not.
   # e.g. If the 'Street' value:key is 'Address', then any warnings about City, State, Zip can be ignored. 
   # Insurance Policy Numbers should be all alphanumeric with no other characters. 
   # Make sure that the name field has at least one name under it (basically check for a blank or 
   # partially blank csv with just a header)
      
    # Display the identified fields and missing fields warnings
    #print("The following Medisoft fields have been identified in the CSV:\n")
    #for header, medisoft_field in identified_fields.items():
    #    print("{0} (CSV header: {1})".format(medisoft_field, header))
    
    #if missing_fields_warnings:
    #    print("\nSome required fields could not be matched:")
    #    for warning in missing_fields_warnings:
    #        print(warning)  

    #print("Debug - Identified fields mapping (intake scan):", identified_fields)
    return identified_fields