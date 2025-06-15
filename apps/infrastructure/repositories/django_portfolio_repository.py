from apps.domain.interfaces.repositories.portfolio_repository import PortfolioRepository
from typing import List
from apps.domain.entities.portfolio import Portfolio
from apps.domain.entities.service import Service
from apps.infrastructure.models.portfolio_models import PortfolioModel, PortfolioServiceModel


class DjangoPortfolioRepository(PortfolioRepository):
    def create(self, portfolio: Portfolio) -> Portfolio:
        portfolio_already_exists = PortfolioModel.objects.filter(professional_id=portfolio.professional_id).exists()
        if portfolio_already_exists:
            raise Exception("Portifolio já existe")
        
        portfolio_model = PortfolioModel.objects.create(
            professional_id=portfolio.professional_id,
            description=portfolio.description,
            image=portfolio.image_url,
        )

        for service in portfolio.services:
            PortfolioServiceModel.objects.create(
                portfolio_id=portfolio_model.id,
                service_id=service.id,
            )

        return portfolio
