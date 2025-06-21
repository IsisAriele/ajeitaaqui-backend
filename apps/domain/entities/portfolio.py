from dataclasses import dataclass
from typing import List

from apps.domain.entities.service import Service


@dataclass
class Portfolio:
    id: int
    professional_id: str
    image_url: str
    description: str
    services: List[Service]
