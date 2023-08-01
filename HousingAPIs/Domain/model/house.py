from dataclasses import dataclass

@dataclass
class HouseLatLong:
    """
    First we will initalize the class with lat and long
    After that, we will reverse geocode and then add the features later
    """
    lat: float
    long: float