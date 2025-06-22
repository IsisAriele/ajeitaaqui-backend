from apps.domain.entities.portfolio import Portfolio
from apps.domain.exceptions.portfolio_exceptions import PortfolioException
from apps.domain.interfaces.repositories.portfolio_repository import PortfolioRepository


class DetailPortfolioUseCase:
    def __init__(
        self,
        portfolio_repository: PortfolioRepository,
    ):
        self.portfolio_repository = portfolio_repository

    def get_portfolio(self, portfolio_id: str) -> Portfolio:
        try:
            portfolio = self.portfolio_repository.get(portfolio_id)
        except Exception as e:
            raise PortfolioException(str(e))

        return portfolio
