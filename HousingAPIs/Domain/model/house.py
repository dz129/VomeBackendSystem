from dataclasses import dataclass

@dataclass
class House:
    """
    First we will initalize the class with lat and long
    After that, we will reverse geocode and then add the features later
    """
    lat: float
    long: float
    streetAddress: string
    zip: string
    city: string
    country: string

    def __init__(self, lat: float, long: float):
        self.lat = lat
        self.long = long
