from dataclasses import dataclass


@dataclass
class Category:
    id: int
    description: str
    icon_url: str = None
