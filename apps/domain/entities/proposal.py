from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List

from apps.domain.entities.professional import Client, Professional


class ProposalStatus(str, Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    REJECTED = "REJECTED"


@dataclass
class Proposal:
    id: int
    value: float
    scheduled_datetime: datetime
    client: Client
    professional: Professional
    services: List[int]
    status: ProposalStatus = ProposalStatus.PENDING
