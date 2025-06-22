from django.test import TestCase

from apps.domain.entities.portfolio import Portfolio
from apps.domain.exceptions.portfolio_exceptions import PortfolioException
from apps.domain.exceptions.professional_exceptions import ProfessionalException
from apps.domain.exceptions.service_exceptions import ServiceException
from apps.domain.usecases.manage_portfolio_use_case import ManagePortfolioUseCase
from apps.infrastructure.models import (
    CategoryModel,
    ClientModel,
    PortfolioModel,
    PortfolioServiceModel,
    ProfessionalModel,
    ServiceModel,
)
from apps.infrastructure.repositories.django_portfolio_repository import DjangoPortfolioRepository
from apps.infrastructure.repositories.django_professional_repository import DjangoProfessionalRepository
from apps.infrastructure.repositories.django_service_repository import DjangoServiceRepository


class TestManagePortfolioUseCase(TestCase):
    def setUp(self):
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

        for i in range(1, 4):
            ServiceModel.objects.create(
                category=self.category_model,
                description=f"Service {i}",
            )

    def test_should_create_portfolio_success(self):
        portfolio = Portfolio(
            id=None,
            professional_id=self.professional_model.id,
            image_url="http://example.com/image.jpg",
            description="This is a test portfolio",
            services=[1, 2, 3],
        )

        use_case = ManagePortfolioUseCase(
            DjangoProfessionalRepository(), DjangoPortfolioRepository(), DjangoServiceRepository()
        )

        use_case.create_portfolio(portfolio)

        self.assertTrue(PortfolioModel.objects.filter(professional=self.professional_model).exists())

    def test_create_should_raise_exception_when_professional_not_found(self):
        portfolio = Portfolio(
            id=None,
            professional_id="999",  # Non-existent professional ID
            image_url="http://example.com/image.jpg",
            description="This is a test portfolio",
            services=[1, 2, 3],
        )

        use_case = ManagePortfolioUseCase(
            DjangoProfessionalRepository(), DjangoPortfolioRepository(), DjangoServiceRepository()
        )

        with self.assertRaises(ProfessionalException) as context:
            use_case.create_portfolio(portfolio)

        self.assertEqual(str(context.exception), "Professional not found.")

    def test_create_should_raise_exception_when_service_not_found(self):
        portfolio = Portfolio(
            id=None,
            professional_id=self.professional_model.id,
            image_url="http://example.com/image.jpg",
            description="This is a test portfolio",
            services=[999],  # Non-existent service ID
        )

        use_case = ManagePortfolioUseCase(
            DjangoProfessionalRepository(), DjangoPortfolioRepository(), DjangoServiceRepository()
        )

        with self.assertRaises(ServiceException) as context:
            use_case.create_portfolio(portfolio)

        self.assertEqual(str(context.exception), "Service with id 999 does not exist.")

    def test_should_raise_exception_when_portfolio_already_exists(self):
        portfolio_model = PortfolioModel.objects.create(
            professional=self.professional_model,
            description="This is a test portfolio",
        )

        portfolio = Portfolio(
            id=portfolio_model.id,
            professional_id=self.professional_model.id,
            image_url="http://example.com/image.jpg",
            description="This is a test portfolio",
            services=[1],
        )

        use_case = ManagePortfolioUseCase(
            DjangoProfessionalRepository(), DjangoPortfolioRepository(), DjangoServiceRepository()
        )

        with self.assertRaises(Exception) as context:
            use_case.create_portfolio(portfolio)

        self.assertIn("Portfolio already exists for this professional.", str(context.exception))

    def test_should_update_portfolio_success(self):
        portfolio = Portfolio(
            id=None,
            professional_id=self.professional_model.id,
            image_url="http://example.com/image.jpg",
            description="This is a test portfolio",
            services=[1, 2, 3],
        )

        use_case = ManagePortfolioUseCase(
            DjangoProfessionalRepository(), DjangoPortfolioRepository(), DjangoServiceRepository()
        )

        use_case.create_portfolio(portfolio)
        self.assertEqual(PortfolioServiceModel.objects.filter(service_id__in=[1, 2, 3]).count(), 3)

        new_portfolio = Portfolio(
            id=None,
            professional_id=self.professional_model.id,
            image_url="http://example.com/image.jpg",
            description="New description for the portfolio",
            services=[3],
        )

        use_case.update_portfolio(new_portfolio)

        portfolio_model = PortfolioModel.objects.get(professional=self.professional_model)

        self.assertEqual(
            PortfolioServiceModel.objects.filter(portfolio=portfolio_model, service_id__in=[1, 2, 3]).count(), 1
        )
        self.assertEqual(portfolio_model.description, new_portfolio.description)

    def test_update_should_raise_exception_when_professional_not_found(self):
        portfolio = Portfolio(
            id=None,
            professional_id="999",  # Non-existent professional ID
            image_url="http://example.com/image.jpg",
            description="This is a test portfolio",
            services=[1, 2, 3],
        )

        use_case = ManagePortfolioUseCase(
            DjangoProfessionalRepository(), DjangoPortfolioRepository(), DjangoServiceRepository()
        )

        with self.assertRaises(ProfessionalException) as context:
            use_case.update_portfolio(portfolio)

        self.assertEqual(str(context.exception), "Professional not found.")

    def test_update_should_raise_exception_when_service_not_found(self):
        portfolio = Portfolio(
            id=None,
            professional_id=self.professional_model.id,
            image_url="http://example.com/image.jpg",
            description="This is a test portfolio",
            services=[999],  # Non-existent service ID
        )

        use_case = ManagePortfolioUseCase(
            DjangoProfessionalRepository(), DjangoPortfolioRepository(), DjangoServiceRepository()
        )

        with self.assertRaises(ServiceException) as context:
            use_case.update_portfolio(portfolio)

        self.assertEqual(str(context.exception), "Service with id 999 does not exist.")

    def test_get_portfolio_by_client_id_test_should_create_portfolio_success(self):
        portfolio = Portfolio(
            id=None,
            professional_id=self.professional_model.id,
            image_url="http://example.com/image.jpg",
            description="This is a test portfolio",
            services=[1, 2, 3],
        )

        use_case = ManagePortfolioUseCase(
            DjangoProfessionalRepository(), DjangoPortfolioRepository(), DjangoServiceRepository()
        )

        use_case.create_portfolio(portfolio)

        retrieved_portfolio = use_case.get_portfolio_by_client_id(self.client_model.id)

        self.assertIsNotNone(retrieved_portfolio)
        self.assertEqual(retrieved_portfolio.professional_id, self.professional_model.id)
        self.assertEqual(retrieved_portfolio.description, portfolio.description)

    def test_get_portfolio_by_client_id_should_raise_exception_when_portfolio_not_found(self):
        client_model = ClientModel.objects.create(
            id="2",
            first_name="Nome",
            last_name="Sobrenome",
            birth_date="1999-12-31",
            document="xxx.xxx.xxx-xy",
            email="nome1@ifrn.com.br",
            username="nome1@ifrn.com.br",
            phone="8499999-9998",
            city="Natal",
            state="RN",
            zip_code="59000-000",
            country="BR",
            photo=None,
            password="123mudar",
        )

        ProfessionalModel.objects.create(
            client=client_model,
        )

        use_case = ManagePortfolioUseCase(
            DjangoProfessionalRepository(), DjangoPortfolioRepository(), DjangoServiceRepository()
        )

        with self.assertRaises(PortfolioException) as context:
            use_case.get_portfolio_by_client_id(client_model.id)
