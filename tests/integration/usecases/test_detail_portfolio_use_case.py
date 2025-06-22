from django.test import TestCase

from apps.domain.entities.portfolio import Portfolio
from apps.domain.usecases.detail_portfolio_use_case import DetailPortfolioUseCase
from apps.infrastructure.models import (
    CategoryModel,
    ClientModel,
    PortfolioModel,
    PortfolioServiceModel,
    ProfessionalModel,
    ServiceModel,
)
from apps.infrastructure.repositories.django_portfolio_repository import DjangoPortfolioRepository


class TestDetailPortfolioUseCase(TestCase):
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

        self.portfolio_model = PortfolioModel.objects.create(
            professional=self.professional_model,
            description="This is a test portfolio",
            image="http://example.com/image.jpg",
        )

        for i in range(1, 4):
            service_model = ServiceModel.objects.create(
                category=self.category_model,
                description=f"Service {i}",
            )
            PortfolioServiceModel.objects.create(
                portfolio=self.portfolio_model,
                service=service_model,
            )

    def test_should_get_portfolio_detail_success(self):
        use_case = DetailPortfolioUseCase(
            DjangoPortfolioRepository(),
        )

        portfolio = use_case.get_portfolio(self.portfolio_model.id)

        self.assertIsInstance(portfolio, Portfolio)
        self.assertEqual(portfolio.id, self.portfolio_model.id)
        self.assertEqual(portfolio.professional_id, self.professional_model.id)
        self.assertEqual(portfolio.description, "This is a test portfolio")
        self.assertEqual(len(portfolio.services), 3)
