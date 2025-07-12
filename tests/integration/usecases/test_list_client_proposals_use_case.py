from datetime import datetime, timezone

from django.test import TestCase

from apps.domain.usecases.list_client_proposals_use_case import ListClientProposalsUseCase
from apps.infrastructure.models import (
    CategoryModel,
    ClientModel,
    ProfessionalModel,
    ProposalModel,
    ProposalServiceModel,
    ServiceModel,
)
from apps.infrastructure.repositories.django_client_repository import DjangoClientRepository
from apps.infrastructure.repositories.django_proposal_repository import DjangoProposalRepository


class ListClientProposalsUseCaseIntegrationTest(TestCase):
    def setUp(self):
        self.category = CategoryModel.objects.create(description="Beleza")
        self.service = ServiceModel.objects.create(category=self.category, description="Corte Feminino")
        self.client_user = ClientModel.objects.create_user(
            id="1",
            username="cliente@ifrn.com.br",
            email="cliente@ifrn.com.br",
            password="senha123",
            first_name="Cliente",
            last_name="Teste",
        )
        self.professional = ProfessionalModel.objects.create(client=self.client_user)
        self.proposal = ProposalModel.objects.create(
            client=self.client_user,
            professional=self.professional,
            value=100.0,
            scheduled_datetime=datetime(2025, 7, 12, 10, 0, 0),
        )
        ProposalServiceModel.objects.create(
            proposal=self.proposal,
            service=self.service,
        )
        self.proposal_repository = DjangoProposalRepository()
        self.client_repository = DjangoClientRepository()
        self.use_case = ListClientProposalsUseCase(self.proposal_repository, self.client_repository)

    def test_list_client_proposals(self):
        proposals = self.use_case.list_all(self.client_user.id)
        self.assertEqual(len(proposals), 1)
        proposal = proposals[0]
        self.assertEqual(proposal.client.id, self.client_user.id)
        self.assertEqual(proposal.value, 100.0)
        self.assertEqual(proposal.scheduled_datetime, datetime(2025, 7, 12, 10, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(proposal.services[0].description, "Corte Feminino")
