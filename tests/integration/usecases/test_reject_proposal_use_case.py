from datetime import datetime

from django.test import TestCase

from apps.domain.entities.proposal import ProposalStatus
from apps.domain.usecases.reject_proposal_use_case import RejectProposalUseCase
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


class RejectProposalUseCaseIntegrationTest(TestCase):
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
        self.use_case = RejectProposalUseCase(self.proposal_repository, self.client_repository)

    def test_reject_proposal_success(self):
        self.assertEqual(self.proposal.status, ProposalStatus.PENDING)
        self.use_case.reject(self.client_user.id, self.proposal.id)
        self.proposal.refresh_from_db()
        self.assertEqual(self.proposal.status, ProposalStatus.REJECTED)

    def test_reject_proposal_not_found(self):
        with self.assertRaises(Exception) as err:
            self.use_case.reject(self.client_user.id, 999)

        self.assertEqual(str(err.exception), "Proposal not found or does not belong to the client.")
