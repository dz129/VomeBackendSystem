from dataclasses import dataclass

@dataclass
class AddressResponse:
    street: str
    houseNumber: str
    city: str
    state: str
    zip: str
