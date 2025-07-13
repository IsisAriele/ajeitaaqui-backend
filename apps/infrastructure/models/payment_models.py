from django.db import models

from apps.infrastructure.models.proposal_models import ProposalModel


class PaymentModel(models.Model):
    proposal = models.ForeignKey(ProposalModel, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_date = models.DateTimeField()

    def __str__(self):
        return f"Payment {self.transaction_id} - R$ {self.amount}"
