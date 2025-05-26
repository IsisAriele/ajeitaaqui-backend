from dataclasses import dataclass


@dataclass
class Offer:
    id: int
    image_url: str
    description: str
