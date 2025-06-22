import unittest
from unittest.mock import Mock

from apps.domain.entities.portfolio import Portfolio
from apps.domain.exceptions.portfolio_exceptions import PortfolioException
from apps.domain.interfaces.repositories.portfolio_repository import PortfolioRepository
from apps.domain.usecases.detail_portfolio_use_case import DetailPortfolioUseCase


class TestDetailPortfolioUseCase(unittest.TestCase):
    def setUp(self):
        self.portfolio = Portfolio(
            id=1,
            professional_id=1,
            image_url="http://example.com/image.jpg",
            description="This is a test portfolio",
            services=[
                1,
            ],
        )

    def test_should_get_portfolio_by_id_success(self):
        mock_portfolio_repository = Mock(spec=PortfolioRepository)
        use_case = DetailPortfolioUseCase(mock_portfolio_repository)

        mock_portfolio_repository.get.return_value = self.portfolio
        result = use_case.get_portfolio(1)

        self.assertEqual(result, self.portfolio)
        mock_portfolio_repository.get.assert_called_once_with(1)

    def test_get_portfolio_should_raise_exception_when_not_found(self):
        mock_portfolio_repository = Mock(spec=PortfolioRepository)
        use_case = DetailPortfolioUseCase(mock_portfolio_repository)

        mock_portfolio_repository.get.side_effect = PortfolioException("Portfolio not found")

        with self.assertRaises(PortfolioException) as context:
            use_case.get_portfolio(999)

        self.assertEqual(str(context.exception), "Portfolio not found")
        mock_portfolio_repository.get.assert_called_once_with(999)
