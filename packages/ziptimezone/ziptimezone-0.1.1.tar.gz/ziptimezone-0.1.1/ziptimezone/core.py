from timezonefinder import TimezoneFinder
import pgeocode
import pandas as pd
from .mappings import map_timezone_to_region

def get_timezone_by_zip(zip_code, country='US'):
    """
    Retrieve the timezone based on the provided ZIP code.

    This function uses geographic coordinates obtained from a ZIP code
    to determine the corresponding timezone using the TimezoneFinder library.

    Parameters:
        zip_code (str): The ZIP code for which the timezone is requested.
        country (str): The country code, default is 'US', used to refine the search.

    Returns:
        str: The timezone string (e.g., 'America/New_York') if found,
             returns 'Unknown' if the timezone cannot be determined.

    Raises:
        ValueError: If no geographic coordinates can be determined for the given ZIP code.
    """
    nomi = pgeocode.Nominatim(country)
    location = nomi.query_postal_code(zip_code)
    
    if location is not None and not pd.isna(location.latitude):
        latitude, longitude = location.latitude, location.longitude
        tf = TimezoneFinder()
        timezone = tf.timezone_at(lat=latitude, lng=longitude)
        if timezone:
            return map_timezone_to_region(timezone)
        else:
            return 'Unknown'
    else:
        raise ValueError(f"No valid geographic coordinates found for ZIP code {zip_code}.")
