def dms_to_decimal(degrees, minutes, seconds, direction):
    """
    Convert DMS (Degrees, Minutes, Seconds) to Decimal Degrees.
    
    Parameters:
        degrees (int): Degrees part of the coordinate
        minutes (int): Minutes part of the coordinate
        seconds (float): Seconds part of the coordinate
        direction (str): 'N', 'S', 'E', or 'W'
        
    Returns:
        float: Decimal degrees
    """
    decimal = degrees + minutes / 60 + seconds / 3600

    if direction.upper() in ['S', 'W']:
        decimal *= -1

    return decimal

# enter your gps values in DMS:
latitude = dms_to_decimal(17, 32, 33.8530, 'N')
longitude = dms_to_decimal(78, 29, 17.1234, 'E')

# Then print the results:
print(f"Latitude in decimal degrees: {latitude}")
print(f"Longitude in decimal degrees: {longitude}")
