from dataclasses import dataclass
from datetime import datetime


@dataclass
class Review:
    id: int
    rating: float
    datetime: datetime
