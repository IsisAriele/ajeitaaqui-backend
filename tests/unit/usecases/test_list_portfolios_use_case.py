import unittest
from unittest.mock import MagicMock

from apps.domain.entities.portfolio import Portfolio
from apps.domain.usecases.list_portfolios_use_case import ListPortfoliosUseCase


class TestListPortfoliosUseCase(unittest.TestCase):
    def test_list_portfolios_returns_all(self):
        mock_portfolio_repository = MagicMock()
        portfolios = [
            Portfolio(id=1, professional_id=1, image_url="img1.jpg", description="desc1", services=[]),
            Portfolio(id=2, professional_id=2, image_url="img2.jpg", description="desc2", services=[]),
        ]
        mock_portfolio_repository.list_all.return_value = portfolios
        use_case = ListPortfoliosUseCase(mock_portfolio_repository)
        result = use_case.list_portfolios()
        self.assertEqual(result, portfolios)
        mock_portfolio_repository.list_all.assert_called_once()
