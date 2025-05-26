from dataclasses import dataclass
from datetime import datetime


@dataclass
class Proposal:
    id: int
    confirmed: bool
    value: float
    datetime: datetime
