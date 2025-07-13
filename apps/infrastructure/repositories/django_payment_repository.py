from apps.domain.entities.payment import Payment
from apps.domain.interfaces.repositories.payment_repository import PaymentRepository
from apps.infrastructure.models import PaymentModel


class DjangoPaymentRepository(PaymentRepository):
    def create_payment(self, payment: Payment) -> Payment:
        payment_model = PaymentModel.objects.create(
            proposal_id=payment.proposal_id,
            amount=payment.amount,
            transaction_id=payment.transaction_id,
            payment_date=payment.payment_date,
        )
        return Payment(
            proposal_id=payment_model.proposal_id,
            amount=payment_model.amount,
            transaction_id=payment_model.transaction_id,
            payment_date=payment_model.payment_date,
        )
