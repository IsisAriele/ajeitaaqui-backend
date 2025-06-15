from dataclasses import dataclass
from apps.domain.entities.service import Service
from apps.domain.entities.professional import Professional
from typing import List

@dataclass
class Portfolio:
    id: int
    professional_id: str
    image_url: str
    description: str
    services: List[Service]
