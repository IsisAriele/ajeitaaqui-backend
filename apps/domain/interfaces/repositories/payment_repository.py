from abc import ABC, abstractmethod

from apps.domain.entities.payment import Payment


class PaymentRepository(ABC):
    @abstractmethod
    def create_payment(self, payment: Payment) -> Payment:
        pass
