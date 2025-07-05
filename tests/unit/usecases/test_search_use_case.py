import unittest
from unittest.mock import MagicMock

from apps.domain.entities.portfolio import Portfolio
from apps.domain.usecases.search_use_case import SearchUseCase


class TestSearchUseCase(unittest.TestCase):
    def setUp(self):
        self.mock_portfolio_repository = MagicMock()
        self.use_case = SearchUseCase(self.mock_portfolio_repository)

    def test_search_by_service_returns_portfolios(self):
        expected = [Portfolio(id=1, professional_id=1, image_url="img1.jpg", description="desc1", services=[])]
        self.mock_portfolio_repository.list_by_service_name.return_value = expected
        result = self.use_case.search_by_service("Corte")
        self.assertEqual(result, expected)
        self.mock_portfolio_repository.list_by_service_name.assert_called_once_with("Corte")

    def test_search_by_professional_returns_portfolios(self):
        expected = [Portfolio(id=2, professional_id=2, image_url="img2.jpg", description="desc2", services=[])]
        self.mock_portfolio_repository.list_by_professional_name.return_value = expected
        result = self.use_case.search_by_professional("Maria")
        self.assertEqual(result, expected)
        self.mock_portfolio_repository.list_by_professional_name.assert_called_once_with("Maria")
