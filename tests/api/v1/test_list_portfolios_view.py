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


class ListPortfoliosViewTests(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.client1 = ClientModel.objects.create(
            id="1",
            first_name="Nome1",
            last_name="Sobrenome1",
            birth_date="1999-12-31",
            document="xxx.xxx.xxx-xx",
            email="nome1@ifrn.com.br",
            username="nome1@ifrn.com.br",
            phone="8499999-9999",
            city="Natal",
            state="RN",
            zip_code="59000-000",
            country="BR",
            photo=None,
            password="123mudar",
        )
        self.client2 = ClientModel.objects.create(
            id="2",
            first_name="Nome2",
            last_name="Sobrenome2",
            birth_date="1998-11-30",
            document="yyy.yyy.yyy-yy",
            email="nome2@ifrn.com.br",
            username="nome2@ifrn.com.br",
            phone="8488888-8888",
            city="Mossoró",
            state="RN",
            zip_code="59600-000",
            country="BR",
            photo=None,
            password="456mudar",
        )
        self.professional1 = ProfessionalModel.objects.create(client=self.client1)
        self.professional2 = ProfessionalModel.objects.create(client=self.client2)
        self.category_model = CategoryModel.objects.create(description="Category 1")
        self.portfolio1 = PortfolioModel.objects.create(
            professional=self.professional1,
            description="Portfolio 1",
            image="http://example.com/image1.jpg",
        )
        self.portfolio2 = PortfolioModel.objects.create(
            professional=self.professional2,
            description="Portfolio 2",
            image="http://example.com/image2.jpg",
        )
        self.service1 = ServiceModel.objects.create(
            category=self.category_model,
            description="Service 1",
        )
        self.service2 = ServiceModel.objects.create(
            category=self.category_model,
            description="Service 2",
        )
        PortfolioServiceModel.objects.create(service=self.service1, portfolio=self.portfolio1)
        PortfolioServiceModel.objects.create(service=self.service2, portfolio=self.portfolio2)

    def test_list_portfolios_success(self):
        url = reverse("list-portfolios")
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        descriptions = [p["description"] for p in response.data]
        self.assertIn("Portfolio 1", descriptions)
        self.assertIn("Portfolio 2", descriptions)
        # Verifica se os serviços estão corretos
        for p in response.data:
            if p["description"] == "Portfolio 1":
                self.assertEqual(len(p["services"]), 1)
                self.assertEqual(p["services"][0]["description"], "Service 1")
            if p["description"] == "Portfolio 2":
                self.assertEqual(len(p["services"]), 1)
                self.assertEqual(p["services"][0]["description"], "Service 2")
