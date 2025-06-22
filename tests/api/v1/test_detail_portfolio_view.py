from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.infrastructure.models import (
    CategoryModel,
    ClientModel,
    PortfolioModel,
    PortfolioServiceModel,
    ProfessionalModel,
    ServiceModel,
)


class DetailPortfolioViewsTests(APITestCase):
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

        self.portfolio_model = PortfolioModel.objects.create(
            professional=self.professional_model,
            description="Test Portfolio",
            image="http://example.com/image.jpg",
        )

        self.available_services = list()
        for i in range(1, 4):
            service_model = ServiceModel.objects.create(
                category=self.category_model,
                description=f"Service {i}",
            )
            self.available_services.append(service_model)
            PortfolioServiceModel.objects.create(service=service_model, portfolio=self.portfolio_model)

    def test_get_portfolio_detail_success(self):
        self.api_client.force_authenticate(user=self.client_model)
        url = reverse("detail-portfolio", kwargs={"portfolio_id": self.portfolio_model.id})
        response = self.api_client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.portfolio_model.id)
        self.assertEqual(response.data["professional_id"], str(self.professional_model.id))
        self.assertEqual(response.data["description"], "Test Portfolio")
        self.assertEqual(len(response.data["services"]), len(self.available_services))

    def test_get_portfolio_detail_not_found(self):
        self.api_client.force_authenticate(user=self.client_model)
        url = reverse("detail-portfolio", kwargs={"portfolio_id": 9999})
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
