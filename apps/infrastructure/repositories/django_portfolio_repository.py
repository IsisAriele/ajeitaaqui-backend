from django.db import models

from apps.domain.entities.portfolio import Portfolio
from apps.domain.entities.service import Service
from apps.domain.interfaces.repositories.portfolio_repository import PortfolioRepository
from apps.infrastructure.models.portfolio_models import PortfolioModel, PortfolioServiceModel


class DjangoPortfolioRepository(PortfolioRepository):
    def create(self, portfolio: Portfolio) -> Portfolio:
        portfolio_already_exists = PortfolioModel.objects.filter(professional_id=portfolio.professional_id).exists()
        if portfolio_already_exists:
            raise Exception("Portfolio already exists for this professional.")

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

    def get_portfolio_by_professional_id(self, professional_id: str) -> Portfolio:
        try:
            portfolio_model = PortfolioModel.objects.get(professional_id=professional_id)
        except PortfolioModel.DoesNotExist:
            raise Exception("Portfolio not found for this professional.")

        return Portfolio(
            id=portfolio_model.id,
            professional_id=portfolio_model.professional_id,
            image_url=portfolio_model.image.url if portfolio_model.image else None,
            description=portfolio_model.description,
            services=[
                Service(id=service.id, description=service.description) for service in portfolio_model.services.all()
            ],
        )

    def update(self, portfolio: Portfolio) -> dict:
        try:
            portfolio_model = PortfolioModel.objects.get(professional_id=portfolio.professional_id)
        except PortfolioModel.DoesNotExist:
            raise Exception("Portfolio not found for this professional.")

        portfolio_model.description = portfolio.description
        portfolio_model.image = portfolio.image_url

        services_ids_to_remove = [
            portfolio_service.service.id for portfolio_service in portfolio_model.portfolio_services.all()
        ]
        for id in services_ids_to_remove:
            PortfolioServiceModel.objects.filter(portfolio_id=portfolio_model.id, service_id=id).delete()

        for service in portfolio.services:
            PortfolioServiceModel.objects.create(
                portfolio_id=portfolio_model.id,
                service_id=service.id,
            )

        portfolio_model.save()

        return portfolio

    def list_all(self):
        portfolios = []
        for portfolio_model in PortfolioModel.objects.all():
            portfolios.append(
                Portfolio(
                    id=portfolio_model.id,
                    professional_id=portfolio_model.professional_id,
                    image_url=portfolio_model.image.url if portfolio_model.image else None,
                    description=portfolio_model.description,
                    services=[
                        Service(id=ps.service.id, description=ps.service.description)
                        for ps in portfolio_model.portfolio_services.all()
                    ],
                )
            )
        return portfolios

    def list_by_service_name(self, service_name: str):
        portfolios = []
        for portfolio_model in PortfolioModel.objects.filter(
            portfolio_services__service__description__icontains=service_name
        ):
            portfolios.append(
                Portfolio(
                    id=portfolio_model.id,
                    professional_id=portfolio_model.professional_id,
                    image_url=portfolio_model.image.url if portfolio_model.image else None,
                    description=portfolio_model.description,
                    services=[
                        Service(id=ps.service.id, description=ps.service.description)
                        for ps in portfolio_model.portfolio_services.all()
                    ],
                )
            )
        return portfolios

    def list_by_professional_name(self, professional_name: str):
        portfolios = []
        for portfolio_model in PortfolioModel.objects.filter(
            models.Q(professional__client__first_name__icontains=professional_name)
            | models.Q(professional__client__last_name__icontains=professional_name)
        ):
            portfolios.append(
                Portfolio(
                    id=portfolio_model.id,
                    professional_id=portfolio_model.professional_id,
                    image_url=portfolio_model.image.url if portfolio_model.image else None,
                    description=portfolio_model.description,
                    services=[
                        Service(id=ps.service.id, description=ps.service.description)
                        for ps in portfolio_model.portfolio_services.all()
                    ],
                )
            )
        return portfolios
