from dataclasses import dataclass
from datetime import datetime


@dataclass
class Payment:
    proposal_id: int
    amount: float
    transaction_id: str
    payment_date: datetime
