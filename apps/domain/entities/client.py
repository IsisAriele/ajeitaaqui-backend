from dataclasses import dataclass


@dataclass
class Client:
    id: int
    first_name: str
    last_name: str
    birth_date: str
    document: str
    email: str
    phone: str
    city: str
    state: str
    zip_code: str
    country: str
    photo: str = None
    password: str = None
