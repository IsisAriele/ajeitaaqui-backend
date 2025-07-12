from datetime import datetime, timezone

from django.test import TestCase

from apps.domain.usecases.list_professional_proposals_use_case import ListProfessionalProposalsUseCase
from apps.infrastructure.models import (
    CategoryModel,
    ClientModel,
    ProfessionalModel,
    ProposalModel,
    ProposalServiceModel,
    ServiceModel,
)
from apps.infrastructure.repositories.django_professional_repository import DjangoProfessionalRepository
from apps.infrastructure.repositories.django_proposal_repository import DjangoProposalRepository


class ListProfessionalProposalsUseCaseIntegrationTest(TestCase):
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
        self.professional_repository = DjangoProfessionalRepository()
        self.use_case = ListProfessionalProposalsUseCase(self.proposal_repository, self.professional_repository)

    def test_list_professional_proposals(self):
        proposals = self.use_case.list_all(self.professional.id)
        self.assertEqual(len(proposals), 1)
        proposal = proposals[0]
        self.assertEqual(proposal.professional.id, self.professional.id)
        self.assertEqual(proposal.value, 100.0)
        self.assertEqual(proposal.scheduled_datetime, datetime(2025, 7, 12, 10, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(proposal.services[0].description, "Corte Feminino")
