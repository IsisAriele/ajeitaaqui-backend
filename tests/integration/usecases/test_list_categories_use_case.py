from django.test import TestCase

from apps.domain.usecases.list_categories_use_case import ListCategoriesUseCase
from apps.infrastructure.models import CategoryModel
from apps.infrastructure.repositories.django_category_repository import DjangoCategoryRepository


class ListCategoriesUseCaseIntegrationTest(TestCase):
    def setUp(self):
        self.category1 = CategoryModel.objects.create(description="Categoria 1")
        self.category2 = CategoryModel.objects.create(description="Categoria 2")

    def test_list_categories_returns_all(self):
        use_case = ListCategoriesUseCase(DjangoCategoryRepository())
        categories = use_case.list_categories()
        descriptions = [c.description for c in categories]
        self.assertEqual(len(categories), 2)
        self.assertIn("Categoria 1", descriptions)
        self.assertIn("Categoria 2", descriptions)
