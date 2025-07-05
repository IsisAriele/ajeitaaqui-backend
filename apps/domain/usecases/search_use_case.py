from typing import List

from apps.domain.entities.portfolio import Portfolio
from apps.domain.interfaces.repositories.portfolio_repository import PortfolioRepository


class SearchUseCase:
    def __init__(self, portfolio_repository: PortfolioRepository):
        self.portfolio_repository = portfolio_repository

    def search_by_service(self, service_name: str) -> List[Portfolio]:
        return self.portfolio_repository.list_by_service_name(service_name)

    def search_by_professional(self, professional_name: str) -> List[Portfolio]:
        return self.portfolio_repository.list_by_professional_name(professional_name)
