from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.domain.entities.proposal import ProposalStatus
from apps.infrastructure.models import (
    CategoryModel,
    ClientModel,
    ProfessionalModel,
    ProposalModel,
    ProposalServiceModel,
    ServiceModel,
)


class ManageProposalsViewTests(APITestCase):
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

    def test_reject_proposal_success(self):
        proposal = ProposalModel.objects.create(
            client=self.client_model,
            professional=self.professional,
            value=150.0,
            scheduled_datetime=timezone.now(),
        )
        ProposalServiceModel.objects.create(
            proposal=proposal,
            service=self.service,
        )
        reject_url = reverse("manage-proposals", args=[proposal.id])
        response = self.api_client.delete(reject_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        proposal.refresh_from_db()
        self.assertEqual(proposal.status, ProposalStatus.REJECTED)

    def test_reject_proposal_not_found(self):
        reject_url = reverse("manage-proposals", args=[999])
        response = self.api_client.delete(reject_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Proposal not found or does not belong to the client.", str(response.data))

    def test_accept_proposal_success(self):
        proposal = ProposalModel.objects.create(
            client=self.client_model,
            professional=self.professional,
            value=150.0,
            scheduled_datetime=timezone.now(),
        )
        ProposalServiceModel.objects.create(
            proposal=proposal,
            service=self.service,
        )
        accept_url = reverse("manage-proposals", args=[proposal.id])
        response = self.api_client.post(accept_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        proposal.refresh_from_db()
        self.assertEqual(proposal.status, ProposalStatus.CONFIRMED)
        self.assertEqual(response.data["proposal_id"], proposal.id)
        self.assertIn("amount", response.data)
        self.assertIn("transaction_id", response.data)
        self.assertIn("payment_date", response.data)

    def test_accept_proposal_not_found(self):
        accept_url = reverse("manage-proposals", args=[999])
        response = self.api_client.post(accept_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Proposal not found or does not belong to the client.", str(response.data))
