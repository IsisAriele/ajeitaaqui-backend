from typing import List

from apps.domain.entities.portfolio import Portfolio
from apps.domain.interfaces.repositories.portfolio_repository import PortfolioRepository


class ListPortfoliosUseCase:
    def __init__(self, portfolio_repository: PortfolioRepository):
        self.portfolio_repository = portfolio_repository

    def list_portfolios(self) -> List[Portfolio]:
        return self.portfolio_repository.list_all()
