from dataclasses import dataclass
from datetime import datetime

from apps.domain.entities.professional import Client, Professional


@dataclass
class Proposal:
    id: int
    value: float
    scheduled_datetime: datetime
    client: Client
    professional: Professional
    services: list[int]
    confirmed: bool = True
