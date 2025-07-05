from django.test import TestCase

from apps.domain.usecases.search_use_case import SearchUseCase
from apps.infrastructure.models import (
    CategoryModel,
    ClientModel,
    PortfolioModel,
    PortfolioServiceModel,
    ProfessionalModel,
    ServiceModel,
)
from apps.infrastructure.repositories.django_portfolio_repository import DjangoPortfolioRepository


class SearchUseCaseIntegrationTest(TestCase):
    def setUp(self):
        self.client1 = ClientModel.objects.create(
            id="1",
            first_name="Ana",
            last_name="Silva",
            birth_date="1990-01-01",
            document="111.111.111-11",
            email="ana@ifrn.com.br",
            username="ana@ifrn.com.br",
            phone="8499999-1111",
            city="Natal",
            state="RN",
            zip_code="59000-000",
            country="BR",
            photo=None,
            password="senha1",
        )
        self.client2 = ClientModel.objects.create(
            id="2",
            first_name="Bruno",
            last_name="Souza",
            birth_date="1992-02-02",
            document="222.222.222-22",
            email="bruno@ifrn.com.br",
            username="bruno@ifrn.com.br",
            phone="8499999-2222",
            city="Mossoró",
            state="RN",
            zip_code="59600-000",
            country="BR",
            photo=None,
            password="senha2",
        )
        self.professional1 = ProfessionalModel.objects.create(client=self.client1)
        self.professional2 = ProfessionalModel.objects.create(client=self.client2)
        self.category = CategoryModel.objects.create(description="Beleza")
        self.service1 = ServiceModel.objects.create(category=self.category, description="Corte Feminino")
        self.service2 = ServiceModel.objects.create(category=self.category, description="Barba")
        self.portfolio1 = PortfolioModel.objects.create(
            professional=self.professional1,
            description="Portfólio Ana",
            image="http://example.com/ana.jpg",
        )
        self.portfolio2 = PortfolioModel.objects.create(
            professional=self.professional2,
            description="Portfólio Bruno",
            image="http://example.com/bruno.jpg",
        )
        PortfolioServiceModel.objects.create(service=self.service1, portfolio=self.portfolio1)
        PortfolioServiceModel.objects.create(service=self.service2, portfolio=self.portfolio2)

    def test_search_by_service_name(self):
        use_case = SearchUseCase(DjangoPortfolioRepository())
        portfolios = use_case.search_by_service("Corte")
        self.assertEqual(len(portfolios), 1)
        self.assertEqual(portfolios[0].description, "Portfólio Ana")
        self.assertEqual(portfolios[0].services[0].description, "Corte Feminino")

    def test_search_by_professional_name_first_name(self):
        use_case = SearchUseCase(DjangoPortfolioRepository())
        portfolios = use_case.search_by_professional("Bruno")
        self.assertEqual(len(portfolios), 1)
        self.assertEqual(portfolios[0].description, "Portfólio Bruno")
        self.assertEqual(portfolios[0].services[0].description, "Barba")

    def test_search_by_professional_name_last_name(self):
        use_case = SearchUseCase(DjangoPortfolioRepository())
        portfolios = use_case.search_by_professional("Silva")
        self.assertEqual(len(portfolios), 1)
        self.assertEqual(portfolios[0].description, "Portfólio Ana")
        self.assertEqual(portfolios[0].services[0].description, "Corte Feminino")

    def test_search_by_service_name_not_found(self):
        use_case = SearchUseCase(DjangoPortfolioRepository())
        portfolios = use_case.search_by_service("Coloração")
        self.assertEqual(len(portfolios), 0)

    def test_search_by_professional_name_not_found(self):
        use_case = SearchUseCase(DjangoPortfolioRepository())
        portfolios = use_case.search_by_professional("Carla")
        self.assertEqual(len(portfolios), 0)
