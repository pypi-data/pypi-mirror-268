import os
import logging
import argparse
import shutil
from datetime import datetime
import glob
import MediLink_ERA_decoder
from MediLink_DataMgmt import operate_winscp
import MediLink_ConfigLoader

"""
We need to make another function that figures out claim rejections and tries to solve them.

1. Config File Path Adjustment: Ensure the configuration file's path is adaptable for various environments, or clearly document the process for setting this path.
2. Logging Enhancements: Improve the logging mechanism to offer comprehensive insights through both file and console outputs, aiding in troubleshooting and operational monitoring.
3. CSV Output Refinement: Update the CSV output structure to include essential ERA data such as Payer Address, ensuring completeness and accuracy of information.
4. CSV Consolidation Logic: Develop logic for intelligently consolidating CSV outputs from batch-processed ERA files, ensuring coherent and comprehensive data aggregation.
5. Secure Endpoint Authentication: Establish a secure method for inputting and storing endpoint authentication details, enhancing script security.
6. Automated Endpoint Processing: Integrate automated looping through configured endpoints for ERA file retrieval, maximizing efficiency and reducing manual oversight.
7. Configuration Key Accuracy: Audit the script to correct any inaccuracies in configuration key references, ensuring seamless configuration data retrieval.
"""

# Setup basic logging
def setup_logger(local_storage_path):
    # Define a reasonable name for the log file, e.g., "MediLink_Down_Process.log"
    log_filename = datetime.now().strftime("MediLink_Down_Process_%m%d%Y.log")
    log_filepath = os.path.join(local_storage_path, log_filename)

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    
    # Setup logging to file
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename=log_filepath,  # Direct logging to a file in local_storage_path
                        filemode='a')  # Append mode

    # If you also want to see the logs in the console, add a StreamHandler
    #console_handler = logging.StreamHandler()
    #console_handler.setLevel(logging.INFO)
    #formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    #console_handler.setFormatter(formatter)
    #logging.getLogger('').addHandler(console_handler)

# Because I can't figure out how to get it to work directly in the WinSCP command.
# And on the Windows XP machine apparently the default path is C:\\ ...
# This needs to get fixed. Ugh.
def move_downloaded_files(local_storage_path):
    # Define the target directory for storing downloaded files
    local_response_directory = os.path.join(local_storage_path, "responses")
    
    if not os.path.exists(local_response_directory):
        os.makedirs(local_response_directory)
    
    # Identify all downloaded .era files in the current directory
    # downloaded_files = [f for f in os.listdir('.') if f.endswith('.era')]
    downloaded_files = [f for f in os.listdir('C:\\Users\\danie\\OneDrive\\Documents') if f.endswith('.era')]
    
    # Move each file to the local_response_directory
    for file in downloaded_files:
        source_path = os.path.join('C:\\Users\\danie\\OneDrive\\Documents', file)
        # source_path = os.path.join('.', file)    for the XP machine? -- This whole thing needs repaired. 
        destination_path = os.path.join(local_response_directory, file)
        shutil.move(source_path, destination_path)
        logging.info("Moved '{}' to '{}'".format(file, local_response_directory))

def find_era_files(era_file_path):
    """
    Find all files matching the era_file_path pattern.
    This function normalizes the path and supports wildcard patterns.
    """
    # Normalize the path to handle slashes correctly
    normalized_path = os.path.normpath(era_file_path)

    # Handling different wildcard scenarios
    if "*" in normalized_path:
        # Use glob to find all files matching the pattern
        matching_files = glob.glob(normalized_path)
        # Normalize paths in the resulting list
        return [os.path.normpath(file) for file in matching_files]
    else:
        # Single file specified, return it in a list if it exists
        return [normalized_path] if os.path.exists(normalized_path) else []

def main(desired_endpoint='AVAILITY'):
    parser = argparse.ArgumentParser(description="Process ERA files and convert them to CSV format.")
    parser.add_argument('--config_path', type=str, help='Path to the configuration JSON file', default="json\\config.json") # Default handling of json path
    parser.add_argument('--desired_endpoint', type=str, help='The desired endpoint key from the configuration.', default=desired_endpoint)
    parser.add_argument('--era_file_path', type=str, help='Optional: Specify a path to an ERA file for direct translation.', default=None)
    args = parser.parse_args()
    
    # Setup Logger, Load configuration and output directory
    config, _ = MediLink_ConfigLoader.load_configuration(args.config_path)
    local_storage_path = config['MediLink_Config']['local_storage_path']
    setup_logger(local_storage_path)
    output_directory = os.path.join(local_storage_path, "translated_csvs")
     
    # Direct ERA file translation if a file path is provided
    if args.era_file_path:
        era_files = find_era_files(args.era_file_path)
        if era_files:
            era_files_str = ', '.join(era_files)
            logging.info("Translating ERA files: {}".format(era_files_str))
            MediLink_ERA_decoder.translate_era_to_csv(era_files, output_directory)
            # Instead of returning a single CSV file path, consolidate here
            consolidate_csv_path = MediLink_ERA_decoder.consolidate_csvs(output_directory)
            logging.info("Translation and consolidation completed.")
            return consolidate_csv_path
        else:
            logging.error("No ERA files found matching: {}".format(args.era_file_path))
            return
    
    # TODO This probably needs to be built into a loop that cycles through all 3 endpoints. 
    # The loop should use the tdqa or whatever the progress bar is called.
    print("Please wait...\n")
    
    # Validate endpoint key
    endpoint_key = args.desired_endpoint
    if endpoint_key not in config['MediLink_Config']['endpoints']:
        logging.error("Endpoint '{}' not found in configuration. Using default 'AVAILITY'.".format(endpoint_key))
        endpoint_key = 'AVAILITY'
    
    # Retrieve endpoint configuration and local storage path
    endpoint_config = config['MediLink_Config']['endpoints'][endpoint_key]
    local_storage_path = config['MediLink_Config']['local_storage_path']
        
    # Download ERA files from the configured endpoint
    downloaded_files = operate_winscp("download", None, endpoint_config, local_storage_path)
    
    # Translate downloaded ERA files to CSV format
    translated_csv_paths = []
    for file in downloaded_files:
        # TODO This needs to add functionality for differentiating between ERA and 277 or 
        # whatever else might be included in the download folders.
        MediLink_ERA_decoder.translate_era_to_csv([file], output_directory)
        csv_file_path = os.path.join(output_directory, os.path.basename(file) + '.csv')
        translated_csv_paths.append(csv_file_path)
        logging.info("Translated ERA to CSV: {}".format(csv_file_path))
    
    # Consolidate new CSVs
    consolidate_csv_path = MediLink_ERA_decoder.consolidate_csvs(output_directory)
    
    # Return the list of translated CSV file paths
    return consolidate_csv_path

if __name__ == "__main__":
    consolidate_csv_path = main()
    if consolidate_csv_path:
        print("CSV File Created: {}".format(consolidate_csv_path))
    else:
        print("No CSV file was created.")