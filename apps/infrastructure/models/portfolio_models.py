from django.db import models

from apps.infrastructure.models.plan_models import PlanModel
from apps.infrastructure.models.professional_models import ProfessionalModel
from apps.infrastructure.models.service_models import ServiceModel


class PortfolioBoosterModel(models.Model):
    professional = models.OneToOneField(ProfessionalModel, on_delete=models.CASCADE, related_name="portfolio_booster")
    plan = models.ForeignKey(PlanModel, on_delete=models.PROTECT, related_name="portfolio_boosters")
    is_active = models.BooleanField(default=False)
    period = models.PositiveIntegerField(help_text="Duração em dias")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"Booster for {self.professional.client.username} - Active: {self.is_active}"


class PortfolioModel(models.Model):
    professional = models.OneToOneField(ProfessionalModel, on_delete=models.CASCADE, related_name="portfolio")
    booster = models.OneToOneField(
        PortfolioBoosterModel, on_delete=models.SET_NULL, null=True, blank=True, related_name="portfolio"
    )
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="portfolio_images/", null=True, blank=True)

    def __str__(self):
        return f"Portfolio of {self.professional.client.username}"


class PortfolioServiceModel(models.Model):
    portfolio = models.ForeignKey(PortfolioModel, on_delete=models.CASCADE, related_name="portfolio_services")
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, related_name="portfolio_services")

    class Meta:
        unique_together = ("portfolio", "service")

    def __str__(self):
        return f"{self.portfolio} - {self.service.description}"
