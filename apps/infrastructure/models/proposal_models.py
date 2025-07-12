from datetime import datetime

from django.db import models

from apps.infrastructure.models.professional_models import ProfessionalModel
from apps.infrastructure.models.service_models import ServiceModel
from apps.infrastructure.models.user_models import ClientModel


class ProposalModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE, related_name="proposals")
    professional = models.ForeignKey(ProfessionalModel, on_delete=models.CASCADE, related_name="proposals")
    confirmed = models.BooleanField(default=False)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    scheduled_datetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Proposal from {self.professional.client.username} to {self.client.username} - R$ {self.value}"


class ProposalServiceModel(models.Model):
    proposal = models.ForeignKey(ProposalModel, on_delete=models.CASCADE, related_name="proposal_services")
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, related_name="proposal_services")

    class Meta:
        unique_together = ("proposal", "service")

    def __str__(self):
        return f"Service '{self.service.description}' in Proposal {self.proposal.id}"
