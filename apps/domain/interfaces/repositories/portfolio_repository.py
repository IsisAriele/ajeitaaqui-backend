from abc import ABC, abstractmethod
from apps.domain.entities.service import Service
from apps.domain.entities.portfolio import Portfolio
from typing import List

class PortfolioRepository(ABC):
    @abstractmethod
    def create(self, portfolio: Portfolio) -> dict:
        pass
