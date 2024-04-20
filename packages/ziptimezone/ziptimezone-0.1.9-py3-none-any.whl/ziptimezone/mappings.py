def map_timezone_to_region(timezone):
    """
    Maps a detailed timezone name to a more general region name.

    Currently it is set to popular regions in US and PR

    This function uses a predefined mapping to convert timezone identifiers
    like 'America/New_York' into more generally understood regional names
    such as 'Eastern', 'Central', etc.

    Parameters:
        timezone (str): The detailed timezone identifier to be mapped.

    Returns:
        str: A general region name (e.g., 'Eastern'), or 'Unknown' if the
             timezone is not recognized or not included in the mapping.

    Example:
        >>> map_timezone_to_region('America/New_York')
        'Eastern'
    """
    mapping = {
        'America/New_York': 'Eastern',
        'America/Detroit': 'Eastern',
        'America/Kentucky/Louisville': 'Eastern',
        'America/Kentucky/Monticello': 'Eastern',
        'America/Indiana/Indianapolis': 'Eastern',
        'America/Indiana/Vincennes': 'Eastern',
        'America/Indiana/Winamac': 'Eastern',
        'America/Indiana/Marengo': 'Eastern',
        'America/Indiana/Petersburg': 'Eastern',
        'America/Indiana/Vevay': 'Eastern',
        'America/Chicago': 'Central',
        'America/Indiana/Tell_City': 'Central',
        'America/Indiana/Knox': 'Central',
        'America/Menominee': 'Central',
        'America/North_Dakota/Center': 'Central',
        'America/North_Dakota/New_Salem': 'Central',
        'America/North_Dakota/Beulah': 'Central',
        'America/Denver': 'Mountain',
        'America/Boise': 'Mountain',
        'America/Phoenix': 'Mountain',
        'America/Los_Angeles': 'Pacific',
        'America/Anchorage': 'Alaska',
        'Pacific/Honolulu': 'Hawaii',
        'America/Puerto_Rico': 'Atlantic'
    }
    return mapping.get(timezone, 'Unknown')
