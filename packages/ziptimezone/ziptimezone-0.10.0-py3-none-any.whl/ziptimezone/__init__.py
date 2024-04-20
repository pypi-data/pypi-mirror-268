"""
The ziptimezone package provides utilities for converting ZIP codes to time zones
and retrieving geographic coordinates (latitude and longitude) based on ZIP codes.

This package includes:
- `get_timezone_by_zip`: Function to convert a ZIP code into a timezone name.
- `map_timezone_to_region`: Function to map detailed timezone names to broader, 
  more general region names (e.g., 'Eastern', 'Central').
- `get_lat_long`: Function to retrieve the latitude and longitude for a given ZIP code.

Example usage:
from ziptimezone import get_timezone_by_zip, get_lat_long_for_zip

# Get the timezone of a ZIP code
timezone = get_timezone_by_zip('85260')

# Get the latitude and longitude of a ZIP code
latitude, longitude = get_lat_long_for_zip('02138')
"""

from .core import get_timezone_by_zip
from .mappings import map_timezone_to_region
from .geocode import get_lat_long_for_zip

__all__ = ['get_timezone_by_zip', 'map_timezone_to_region', 'get_lat_long_for_zip']
