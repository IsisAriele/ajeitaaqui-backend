from django.db import models

from apps.infrastructure.models.proposal_models import ProposalServiceModel
from apps.infrastructure.models.user_models import ClientModel


class ReviewModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE, related_name="reviews")
    proposal_service = models.OneToOneField(ProposalServiceModel, on_delete=models.CASCADE, related_name="review")
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.client.username} - Rating: {self.rating}"
