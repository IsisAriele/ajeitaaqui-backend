from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.infrastructure.models import CategoryModel, ClientModel, PortfolioModel, ProfessionalModel, ServiceModel


class CreatePortfolioViewTests(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.client_model = ClientModel.objects.create(
            id="1",
            first_name="Nome",
            last_name="Sobrenome",
            birth_date="1999-12-31",
            document="xxx.xxx.xxx-xx",
            email="nome@ifrn.com.br",
            phone="8499999-9999",
            city="Natal",
            state="RN",
            zip_code="59000-000",
            country="BR",
            photo=None,
            password="123mudar",
        )

        self.professional_model = ProfessionalModel.objects.create(
            client=self.client_model,
        )

        self.category_model = CategoryModel.objects.create(
            description="Category 1",
        )

        for i in range(1, 4):
            ServiceModel.objects.create(
                category=self.category_model,
                description=f"Service {i}",
            )

        self.url = reverse("create-portfolio")
        self.api_client.force_authenticate(user=self.client_model)

    def test_create_portfolio_success(self):
        response = self.api_client.post(
            self.url,
            data={
                "image_url": "http://example.com/image.jpg",
                "description": "This is a test portfolio",
                "services": [1, 2, 3],
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_portfolio_professional_not_found(self):
        client_without_professional_model = ClientModel.objects.create(
            id="2",
            first_name="Nome1",
            last_name="Sobrenome1",
            birth_date="1999-12-31",
            document="xxx.xxx.xxx-xy",
            email="nome1@ifrn.com.br",
            username="nome1@ifrn.com.br",
            phone="8499999-9998",
            city="Natal",
            state="RN",
            zip_code="59000-000",
            country="BR",
            photo=None,
            password="123mudar",
        )
        self.api_client.force_authenticate(user=client_without_professional_model)

        response = self.api_client.post(
            self.url,
            data={
                "image_url": "http://example.com/image.jpg",
                "description": "This is a test portfolio",
                "services": [1, 2, 3],
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("message", response.data)
        self.assertEqual(response.data["message"], "Professional not found.")

    def test_create_portfolio_service_not_found(self):
        response = self.api_client.post(
            self.url,
            data={
                "image_url": "http://example.com/image.jpg",
                "description": "This is a test portfolio",
                "services": [999],  # Non-existent service ID
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("message", response.data)
        self.assertEqual(response.data["message"], "Service with id 999 does not exist.")

    def test_create_portfolio_already_exists(self):
        PortfolioModel.objects.create(
            professional=self.professional_model,
            image_url="http://example.com/image.jpg",
            description="This is a test portfolio",
        )

        response = self.api_client.post(
            self.url,
            data={
                "image_url": "http://example.com/image.jpg",
                "description": "This is a test portfolio",
                "services": [1, 2, 3],
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("message", response.data)
        self.assertEqual(response.data["message"], "Portfolio already exists for this professional.")
