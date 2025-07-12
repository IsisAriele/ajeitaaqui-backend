from datetime import datetime

from django.test import TestCase

from apps.domain.entities.proposal import Proposal
from apps.domain.usecases.create_proposal_use_case import CreateProposalUseCase
from apps.infrastructure.models import CategoryModel, ClientModel, ProfessionalModel, ServiceModel
from apps.infrastructure.repositories.django_client_repository import DjangoClientRepository
from apps.infrastructure.repositories.django_professional_repository import DjangoProfessionalRepository
from apps.infrastructure.repositories.django_proposal_repository import DjangoProposalRepository
from apps.infrastructure.repositories.django_service_repository import DjangoServiceRepository


class CreateProposalUseCaseIntegrationTest(TestCase):
    def setUp(self):
        self.client = ClientModel.objects.create(
            id="1",
            first_name="Cliente",
            last_name="Teste",
            birth_date="1990-01-01",
            document="111.111.111-11",
            email="cliente@ifrn.com.br",
            phone="8499999-1111",
            city="Natal",
            state="RN",
            zip_code="59000-000",
            country="BR",
            photo=None,
            password="senha1",
        )
        self.professional = ProfessionalModel.objects.create(client=self.client)
        self.category = CategoryModel.objects.create(description="Beleza")
        self.service1 = ServiceModel.objects.create(category=self.category, description="Corte Feminino")
        self.service2 = ServiceModel.objects.create(category=self.category, description="Barba")
        self.proposal_repository = DjangoProposalRepository()
        self.client_repository = DjangoClientRepository()
        self.professional_repository = DjangoProfessionalRepository()
        self.service_repository = DjangoServiceRepository()
        self.use_case = CreateProposalUseCase(
            self.proposal_repository, self.client_repository, self.professional_repository, self.service_repository
        )

    def test_create_proposal_success(self):
        scheduled_datetime = datetime(2025, 7, 12, 10, 0, 0)
        proposal = Proposal(
            id=None,
            client=self.client,
            professional=self.professional,
            services=[self.service1.id, self.service2.id],
            value=150.0,
            scheduled_datetime=scheduled_datetime,
        )
        result = self.use_case.create_proposal(proposal)
        self.assertIsNotNone(result.id)
        self.assertEqual(result.client.id, self.client.id)
        self.assertEqual(result.professional.id, self.professional.id)
        self.assertEqual(len(result.services), 2)
        self.assertEqual(result.services[0].id, self.service1.id)
        self.assertEqual(result.services[1].id, self.service2.id)
        self.assertEqual(result.value, 150.0)
        self.assertEqual(result.scheduled_datetime, scheduled_datetime)
