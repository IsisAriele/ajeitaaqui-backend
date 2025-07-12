from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.infrastructure.models import CategoryModel


class ListCategoriesViewTests(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.category1 = CategoryModel.objects.create(description="Categoria 1")
        self.category2 = CategoryModel.objects.create(description="Categoria 2")

    def test_list_categories_success(self):
        url = reverse("list-categories")
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        descriptions = [c["description"] for c in response.data]
        self.assertIn("Categoria 1", descriptions)
        self.assertIn("Categoria 2", descriptions)
