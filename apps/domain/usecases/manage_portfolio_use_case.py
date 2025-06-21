from typing import List

from apps.domain.entities.portfolio import Portfolio
from apps.domain.exceptions.portfolio_exceptions import PortfolioException
from apps.domain.exceptions.professional_exceptions import ProfessionalException
from apps.domain.exceptions.service_exceptions import ServiceException
from apps.domain.interfaces.repositories.portfolio_repository import PortfolioRepository
from apps.domain.interfaces.repositories.professional_repository import ProfessionalRepository
from apps.domain.interfaces.repositories.service_repository import ServiceRepository


class ManagePortfolioUseCase:
    def __init__(
        self,
        professional_repository: ProfessionalRepository,
        portfolio_repository: PortfolioRepository,
        service_repository: ServiceRepository,
    ):
        self.professional_repository = professional_repository
        self.portfolio_repository = portfolio_repository
        self.service_repository = service_repository

    def create_portfolio(self, portfolio: Portfolio):
        portfolio.professional_id = self.get_professional_id(portfolio.professional_id)
        portfolio.services = self.parse_services(portfolio.services)

        try:
            self.portfolio_repository.create(portfolio)
        except Exception as e:
            raise PortfolioException(str(e))

    def update_portfolio(self, portfolio: Portfolio):
        portfolio.professional_id = self.get_professional_id(portfolio.professional_id)
        portfolio.services = self.parse_services(portfolio.services)

        try:
            self.portfolio_repository.update(portfolio)
        except Exception as e:
            raise PortfolioException(str(e))

    def get_professional_id(self, professional_id: str):
        try:
            return self.professional_repository.get_by_id(professional_id).id
        except Exception as e:
            raise ProfessionalException(str(e))

    def parse_services(self, incomming_services: List[int]):
        if not incomming_services:
            raise PortfolioException("Services list cannot be empty.")

        services = list()
        for service_id in incomming_services:
            try:
                services.append(self.service_repository.get_by_id(service_id))
            except Exception as e:
                raise ServiceException(str(e))

        return services
