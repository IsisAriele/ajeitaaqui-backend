from django.test import TestCase

from apps.domain.entities.portfolio import Portfolio
from apps.domain.exceptions.professional_exceptions import ProfessionalException
from apps.domain.exceptions.service_exceptions import ServiceException
from apps.domain.usecases.manage_portfolio_use_case import ManagePortfolioUseCase
from apps.infrastructure.models import CategoryModel, ClientModel, PortfolioModel, ProfessionalModel, ServiceModel
from apps.infrastructure.repositories.django_portfolio_repository import DjangoPortfolioRepository
from apps.infrastructure.repositories.django_professional_repository import DjangoProfessionalRepository
from apps.infrastructure.repositories.django_service_repository import DjangoServiceRepository


class TestCreateClientUseCase(TestCase):
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

    def test_should_raise_exception_when_professional_not_found(self):
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

    def test_should_raise_exception_when_service_not_found(self):
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
