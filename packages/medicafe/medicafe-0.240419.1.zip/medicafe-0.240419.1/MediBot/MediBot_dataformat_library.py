import re
from datetime import datetime
import re  #for addresses
from MediBot_Preprocessor import open_csv_for_editing, config, initialize
from MediBot_UI import manage_script_pause

# Bring in all the constants
initialize(config)

# Format Data
def format_name(value):  
    if ',' in value:
        return value
    hyphenated_name_pattern = r'(?P<First>[\w-]+)\s+(?P<Middle>[\w-]+)?\s+(?P<Last>[\w-]+)'
    match = re.match(hyphenated_name_pattern, value)
    if match:
        first_name = match.group('First')
        middle_name = match.group('Middle') or ''
        last_name = match.group('Last')
        return '{}, {} {}'.format(last_name, first_name, middle_name).strip()
    parts = value.split()
    return '{}, {}'.format(parts[-1], ' '.join(parts[:-1]))

def format_date(value):
    try:
        date_obj = datetime.strptime(value, '%m/%d/%Y')
        return date_obj.strftime('%m%d%Y')
    except ValueError as e:
        print("Date format error:", e)
        return value

def format_phone(value):
    digits = ''.join(filter(str.isdigit, value))
    if len(digits) == 10:
        return digits
    print("Phone number format error: Invalid number of digits")
    return value

def format_policy(value):
    alphanumeric = ''.join(filter(str.isalnum, value))
    return alphanumeric

def format_gender(value):
    return value[0].upper()

def format_street(value, csv_data, reverse_mapping, parsed_address_components):
    global script_paused
    script_paused = False
    
    # Remove periods from the input (seems to be an XP-only issue?)
    value = value.replace('.', '')
    
    # Only proceed with parsing if a comma is present in the value
    if ',' in value:
        try:
            # Access the common cities from the loaded configuration
            common_cities = config.get('cities', [])

            # Convert cities to a case-insensitive regex pattern
            city_pattern = '|'.join(re.escape(city) for city in common_cities)
            city_regex_pattern = r'(?P<City>{})'.format(city_pattern)
            city_regex = re.compile(city_regex_pattern, re.IGNORECASE)

            # Check if the address contains one of the common cities
            city_match = city_regex.search(value)
                    
            if city_match:
                city = city_match.group('City').upper()  # Normalize city name to uppercase
                street, _, remainder = value.partition(city)

                # Extract state and zip code from the remainder
                address_pattern = r',\s*(?P<State>[A-Z]{2})\s*(?P<Zip>\d{5}(?:-\d{4})?)?'

                match = re.search(address_pattern, remainder)
                    
                if match:
                    # Update global parsed address components
                    parsed_address_components['City'] = city
                    parsed_address_components['State'] = match.group('State')
                    parsed_address_components['Zip Code'] = match.group('Zip')
                    
                    return street.strip()  # Return formatted street address
            else:
                # Fallback to old regex
                # value = street + ', ' + city + remainder
                address_pattern = r'(?P<Street>[\w\s]+),?\s+(?P<City>[\w\s]+),\s*(?P<State>[A-Z]{2})\s*(?P<Zip>\d{5}(-\d{4})?)'
                match = re.match(address_pattern, value)

                if match:
                    # Update global parsed address components
                    parsed_address_components['City'] = match.group('City')
                    parsed_address_components['State'] = match.group('State')
                    parsed_address_components['Zip Code'] = match.group('Zip')

                    return match.group('Street').strip()  # Return formatted street address
                    
        except Exception as e:
            print("Address format error: Unable to parse address '{}'. Error: {}".format(value, e))
            print("Please update the CSV file for this record.")
            script_paused = True
            open_csv_for_editing(CSV_FILE_PATH)  # Offer to open the CSV for manual correction
            manage_script_pause(csv_data, e, reverse_mapping) 
            return value.replace(' ', '{Space}')  # Fallback to return original value with spaces escaped
    else:
        # If no comma is present, return the value as is, assuming it's just a street name
        return value.replace(' ', '{Space}')
    
    # This return acts as a fallback in case the initial comma check passes but no address components are matched
    return value.replace(' ', '{Space}')  

def format_zip(value):
    # Ensure the value is a string, in case it's provided as an integer
    value_str = str(value)
    # Return only the first 5 characters of the zip code
    return value_str[:5]

def format_data(medisoft_field, value, csv_data, reverse_mapping, parsed_address_components):
    if medisoft_field == 'Patient Name':
        formatted_value = format_name(value)
    elif medisoft_field == 'Birth Date':
        formatted_value = format_date(value)
    elif medisoft_field == 'Phone':
        formatted_value = format_phone(value)
    elif medisoft_field == 'Phone #2':
        formatted_value = format_phone(value)
    elif medisoft_field == 'Gender':
        formatted_value = format_gender(value)
    elif medisoft_field == 'Street':
        formatted_value = format_street(value, csv_data, reverse_mapping, parsed_address_components)
    elif medisoft_field == 'Zip Code':
        formatted_value = format_zip(value)
    elif medisoft_field == 'Primary Policy Number':
        formatted_value = format_policy(value)
    elif medisoft_field == 'Secondary Policy Number':
        formatted_value = format_policy(value)
    elif medisoft_field == 'Primary Group Number':
        formatted_value = format_policy(value)
    elif medisoft_field == 'Secondary Group Number':
        formatted_value = format_policy(value)
    else:
        formatted_value = value

    formatted_value = formatted_value.replace(',', '{,}').replace(' ', '{Space}')
    ahk_command = 'SendInput, {}{{Enter}}'.format(formatted_value)
    return ahk_command