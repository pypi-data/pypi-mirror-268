from timezonefinder import TimezoneFinder
import csv
from .data_manager import get_data_file_path
from .mappings import map_timezone_to_region
'''
def load_zip_data():
    """
    Loads ZIP code data from a CSV file into a dictionary.

    Returns:
        dict: A dictionary where the keys are ZIP codes and the values are dictionaries with
              latitude and longitude.
    """
    file_path = get_data_file_path()
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['country_code', 'postal_code', 'place_name', 'admin_name1',
                                                     'admin_code1', 'admin_name2', 'admin_code2', 'admin_name3',
                                                     'admin_code3', 'latitude', 'longitude', 'accuracy'], delimiter='\t')
        zip_data = {row['postal_code']: row for row in reader}
    return zip_data
'''
loaded_zip_data = None

def load_zip_data():
    """
    Loads ZIP code data from a CSV file into a dictionary if it is not already loaded.

    Returns:
        dict: A dictionary where the keys are ZIP codes and the values are dictionaries with
              latitude and longitude.
    """
    global loaded_zip_data
    if loaded_zip_data is not None:
        return loaded_zip_data

    file_path = get_data_file_path()
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['country_code', 'postal_code', 'place_name', 'admin_name1',
                                                     'admin_code1', 'admin_name2', 'admin_code2', 'admin_name3',
                                                     'admin_code3', 'latitude', 'longitude', 'accuracy'], delimiter='\t')
        loaded_zip_data = {row['postal_code']: row for row in reader}
    return loaded_zip_data

def get_timezone_by_zip(zip_code):
    """
    Retrieve the timezone based on the provided ZIP code from locally stored data.

    This function uses geographic coordinates obtained from a ZIP code stored in a local file
    to determine the corresponding timezone using the TimezoneFinder library.

    Parameters:
        zip_code (str): The ZIP code for which the timezone is requested.

    Returns:
        str: The timezone string (e.g., 'America/New_York') if found,
             returns 'Unknown' if the timezone cannot be determined.

    Raises:
        ValueError: If no geographic coordinates can be determined for the given ZIP code.
    """
    zip_data = load_zip_data()
    location = zip_data.get(zip_code)

    if location and location['latitude'] and location['longitude']:
        latitude, longitude = float(location['latitude']), float(location['longitude'])
        tf = TimezoneFinder()
        timezone = tf.timezone_at(lat=latitude, lng=longitude)
        if timezone:
            return map_timezone_to_region(timezone)
        else:
            return 'Unknown'
    else:
        raise ValueError(f"No valid geographic coordinates found for ZIP code {zip_code}.")