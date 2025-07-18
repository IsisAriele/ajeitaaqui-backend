from abc import ABC, abstractmethod
from typing import List

from apps.domain.entities.portfolio import Portfolio


class PortfolioRepository(ABC):
    @abstractmethod
    def create(self, portfolio: Portfolio) -> dict:
        pass

    @abstractmethod
    def get_portfolio_by_professional_id(self, professional_id: str) -> Portfolio:
        pass

    @abstractmethod
    def update(self, portfolio: Portfolio) -> dict:
        pass

    @abstractmethod
    def list_all(self) -> List[Portfolio]:
        pass

    @abstractmethod
    def list_by_service_name(self, service_name: str) -> List[Portfolio]:
        pass

    @abstractmethod
    def list_by_professional_name(self, professional_name: str) -> List[Portfolio]:
        pass
