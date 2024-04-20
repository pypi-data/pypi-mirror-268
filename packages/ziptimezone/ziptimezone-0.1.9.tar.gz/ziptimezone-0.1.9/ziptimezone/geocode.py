import pgeocode
import pandas as pd

def get_lat_long_for_zip(zip_code, country='US'):
    """
    Retrieve the latitude and longitude for a given ZIP code.

    Parameters:
        zip_code (str): The ZIP code for which geographic coordinates are requested.
        country (str): Country code to refine the search, default is 'US'.

    Returns:
        tuple: A tuple containing latitude and longitude (float, float) if found, otherwise (None, None).

    Raises:
        ValueError: If the zip_code is not recognized.
    """

    if not isinstance(zip_code, str) or zip_code.strip() == '':
        # Return None if the zip_code is not a string or is an empty string.
        return None, None
    
    nomi = pgeocode.Nominatim(country)
    location = nomi.query_postal_code(zip_code)
    
    if location is not None and not pd.isna(location.latitude) and not pd.isna(location.longitude):
        return location.latitude, location.longitude
    else:
        #raise ValueError(f"ZIP code {zip_code} not recognized.")
        return None, None
