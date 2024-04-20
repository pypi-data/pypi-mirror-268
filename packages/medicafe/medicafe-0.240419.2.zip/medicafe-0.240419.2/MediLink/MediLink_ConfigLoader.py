import os
import json
import logging
from datetime import datetime
from collections import OrderedDict
import sys

"""
This function should be generalizable to have a initialization script over all the Medi* functions
"""

# Setup basic logging. 
# BUG Consolidate this with MediLink_837p_encoder_library.log
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

def load_configuration(config_path=os.path.join(os.path.dirname(__file__), '..', 'json', 'config.json'), crosswalk_path=os.path.join(os.path.dirname(__file__), '..', 'json', 'crosswalk.json')):
    """
    Loads endpoint configuration, credentials, and other settings from JSON files.
        
    Returns: A tuple containing dictionaries with configuration settings for the main config and crosswalk.
    """
    # BUG HARDCODE FOR NOW
    config_path="G:\\My Drive\\Codes\\MediCafe\\json\\config.json"
    # "F:\\Medibot\\json\\config.json"
    crosswalk_path="G:\\My Drive\\Codes\\MediCafe\\json\\crosswalk.json"
    # "F:\\Medibot\\json\\crosswalk.json"
    
    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file, object_pairs_hook=OrderedDict)
            if 'MediLink_Config' not in config:
                raise KeyError("MediLink_Config key is missing from the loaded configuration.")
            # MediLink_config = config['MediLink_Config']

        with open(crosswalk_path, 'r') as crosswalk_file:
            crosswalk = json.load(crosswalk_file)

        return config, crosswalk
    except json.JSONDecodeError as e:
        print("Error parsing JSON file: {}".format(e))
        sys.exit(1)  # Exit the script due to a critical error in configuration loading
    except FileNotFoundError:
        print("One or both JSON files not found. Config: {}, Crosswalk: {}".format(config_path, crosswalk_path))
        sys.exit(1)  # Exit the script due to a critical error in configuration loading
    except KeyError as e:
        print("Critical configuration is missing: {}".format(e))
        sys.exit(1)  # Exit the script due to a critical error in configuration loading
    except Exception as e:
        print("An unexpected error occurred while loading the configuration: {}".format(e))
        sys.exit(1)  # Exit the script due to a critical error in configuration loading