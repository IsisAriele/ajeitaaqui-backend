import unittest
from unittest.mock import MagicMock

from apps.domain.entities.category import Category
from apps.domain.usecases.list_categories_use_case import ListCategoriesUseCase


class TestListCategoriesUseCase(unittest.TestCase):
    def test_list_categories_returns_all(self):
        mock_category_repository = MagicMock()
        categories = [
            Category(id=1, description="Categoria 1"),
            Category(id=2, description="Categoria 2"),
        ]
        mock_category_repository.list_all.return_value = categories
        use_case = ListCategoriesUseCase(mock_category_repository)
        result = use_case.list_categories()
        self.assertEqual(result, categories)
        mock_category_repository.list_all.assert_called_once()
