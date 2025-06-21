import unittest
from unittest.mock import Mock

from apps.domain.entities.portfolio import Portfolio
from apps.domain.entities.professional import Professional
from apps.domain.entities.service import Service
from apps.domain.exceptions.professional_exceptions import ProfessionalException
from apps.domain.exceptions.service_exceptions import ServiceException
from apps.domain.interfaces.repositories.portfolio_repository import PortfolioRepository
from apps.domain.interfaces.repositories.professional_repository import ProfessionalRepository
from apps.domain.interfaces.repositories.service_repository import ServiceRepository
from apps.domain.usecases.manage_portfolio_use_case import ManagePortfolioUseCase


class TestManagePortfolioUseCase(unittest.TestCase):
    def setUp(self):
        self.portfolio = Portfolio(
            id=1,
            professional_id=1,
            image_url="http://example.com/image.jpg",
            description="This is a test portfolio",
            services=[
                1,
            ],
        )

        self.professional = Professional(
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

        self.service = Service(id=1, description="Description 1")

    def test_should_create_portfolio_success(self):
        mock_professional_repository = Mock(spec=ProfessionalRepository)
        mock_portfolio_repository = Mock(spec=PortfolioRepository)
        mock_service_repository = Mock(spec=ServiceRepository)

        use_case = ManagePortfolioUseCase(
            mock_professional_repository, mock_portfolio_repository, mock_service_repository
        )
        mock_professional_repository.get_by_id.return_value = self.professional
        mock_service_repository.get_by_id.return_value = self.service
        use_case.create_portfolio(self.portfolio)

        mock_portfolio_repository.create.assert_called_once_with(self.portfolio)

    def test_should_raise_exception_when_professional_not_found(self):
        mock_professional_repository = Mock(spec=ProfessionalRepository)
        mock_portfolio_repository = Mock(spec=PortfolioRepository)
        mock_service_repository = Mock(spec=ServiceRepository)

        use_case = ManagePortfolioUseCase(
            mock_professional_repository, mock_portfolio_repository, mock_service_repository
        )
        mock_professional_repository.get_by_id.side_effect = Exception("Professional not found")

        with self.assertRaises(ProfessionalException) as context:
            use_case.create_portfolio(self.portfolio)

        self.assertEqual(str(context.exception), "Professional not found")

    def test_should_raise_exception_when_service_not_found(self):
        mock_professional_repository = Mock(spec=ProfessionalRepository)
        mock_portfolio_repository = Mock(spec=PortfolioRepository)
        mock_service_repository = Mock(spec=ServiceRepository)

        use_case = ManagePortfolioUseCase(
            mock_professional_repository, mock_portfolio_repository, mock_service_repository
        )
        mock_professional_repository.get_by_id.return_value = self.professional
        mock_service_repository.get_by_id.side_effect = Exception("Service not found")

        with self.assertRaises(ServiceException) as context:
            use_case.create_portfolio(self.portfolio)

        self.assertEqual(str(context.exception), "Service not found")
