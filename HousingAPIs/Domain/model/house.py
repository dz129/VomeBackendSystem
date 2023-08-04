from dataclasses import dataclass

@dataclass
class HouseLatLong:
    """
    to create this class we will combine addressresponse and latlongresponse
    """
    lat: float
    long: float
    street: str
    houseNumber: str
    city: str
    state: str
    zip: str