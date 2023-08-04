from dataclasses import dataclass

@dataclass
class AddressResponse:
    street: str
    houseNumber: str
    city: str
    zip: str
