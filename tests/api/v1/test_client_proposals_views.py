from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.infrastructure.models import (
    CategoryModel,
    ClientModel,
    ProfessionalModel,
    ProposalModel,
    ProposalServiceModel,
    ServiceModel,
)


class ClientProposalsViewTests(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.category = CategoryModel.objects.create(description="Beleza")
        self.service = ServiceModel.objects.create(category=self.category, description="Corte Feminino")
        self.client_model = ClientModel.objects.create_user(
            id="1",
            username="cliente@ifrn.com.br",
            email="cliente@ifrn.com.br",
            password="senha123",
            first_name="Cliente",
            last_name="Teste",
        )
        self.professional = ProfessionalModel.objects.create(client=self.client_model)
        self.api_client.force_authenticate(user=self.client_model)
        self.url = reverse("client-proposals")

    def test_list_client_proposals_success(self):
        proposal = ProposalModel.objects.create(
            client=self.client_model,
            professional=self.professional,
            value=150.0,
            scheduled_datetime=datetime(2025, 7, 12, 10, 0, 0),
        )
        ProposalServiceModel.objects.create(
            proposal=proposal,
            service=self.service,
        )
        response = self.api_client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["value"], 150.0)
        self.assertEqual(response.data[0]["scheduled_datetime"], "2025-07-12T10:00:00Z")
        self.assertEqual(response.data[0]["services"][0]["description"], "Corte Feminino")

    def test_list_client_proposals_empty(self):
        response = self.api_client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_list_client_proposals_unauthenticated(self):
        self.api_client.force_authenticate(user=None)
        response = self.api_client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
