from abc import ABC, abstractmethod

from apps.domain.entities.portfolio import Portfolio


class PortfolioRepository(ABC):
    @abstractmethod
    def create(self, portfolio: Portfolio) -> dict:
        pass
