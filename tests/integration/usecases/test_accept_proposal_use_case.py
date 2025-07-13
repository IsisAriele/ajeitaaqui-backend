from django.test import TestCase
from django.utils import timezone

from apps.domain.entities.payment import Payment
from apps.domain.entities.proposal import ProposalStatus
from apps.domain.usecases.accept_proposal_use_case import AcceptProposalUseCase
from apps.infrastructure.models import (
    CategoryModel,
    ClientModel,
    ProfessionalModel,
    ProposalModel,
    ProposalServiceModel,
    ServiceModel,
)
from apps.infrastructure.repositories.django_client_repository import DjangoClientRepository
from apps.infrastructure.repositories.django_payment_repository import DjangoPaymentRepository
from apps.infrastructure.repositories.django_proposal_repository import DjangoProposalRepository


class AcceptProposalUseCaseIntegrationTest(TestCase):
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
            scheduled_datetime=timezone.now(),
        )
        ProposalServiceModel.objects.create(
            proposal=self.proposal,
            service=self.service,
        )
        self.proposal_repository = DjangoProposalRepository()
        self.client_repository = DjangoClientRepository()
        self.payment_repository = DjangoPaymentRepository()
        self.use_case = AcceptProposalUseCase(self.proposal_repository, self.payment_repository, self.client_repository)

    def test_accept_proposal_success(self):
        result = self.use_case.accept(self.client_user.id, self.proposal.id)
        self.assertTrue(isinstance(result, Payment))
        self.proposal.refresh_from_db()
        self.assertEqual(self.proposal.status, ProposalStatus.CONFIRMED)

    def test_accept_proposal_not_found(self):
        with self.assertRaises(Exception):
            self.use_case.accept(self.client_user.id, 999)
