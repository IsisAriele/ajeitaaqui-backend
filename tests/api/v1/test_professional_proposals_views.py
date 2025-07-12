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


class ProfessionalProposalsViewTests(APITestCase):
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
        self.url = reverse("professional-proposals")

    def test_create_proposal_success(self):
        proposal_data = {
            "client_id": self.client_model.id,
            "services": [self.service.id],
            "value": 100.00,
            "scheduled_datetime": datetime.now().isoformat(),
        }
        response = self.api_client.post(self.url, proposal_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(ProposalModel.objects.filter(client=self.client_model, professional=self.professional).exists())

    def test_create_proposal_invalid_data(self):
        proposal_data = {}
        response = self.api_client.post(self.url, proposal_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {
                "value": ["This field is required."],
                "scheduled_datetime": ["This field is required."],
                "client_id": ["This field is required."],
                "services": ["This field is required."],
            },
        )
        self.assertFalse(ProposalModel.objects.filter(client=self.client_model, professional=self.professional))

    def test_list_professional_proposals_success(self):
        # Cria uma proposta para o profissional autenticado
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

    def test_list_professional_proposals_empty(self):
        response = self.api_client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
