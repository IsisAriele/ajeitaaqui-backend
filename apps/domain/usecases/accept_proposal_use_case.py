from uuid import uuid4

from django.utils import timezone

from apps.domain.entities.payment import Payment
from apps.domain.entities.proposal import Proposal
from apps.domain.interfaces.repositories.client_repository import ClientRepository
from apps.domain.interfaces.repositories.payment_repository import PaymentRepository
from apps.domain.interfaces.repositories.proposal_repository import ProposalRepository


class AcceptProposalUseCase:
    def __init__(
        self,
        proposal_repository: ProposalRepository,
        payment_repository: PaymentRepository,
        client_repository: ClientRepository,
    ):
        self.proposal_repository = proposal_repository
        self.client_repository = client_repository
        self.payment_repository = payment_repository

    def accept(self, client_id: str, proposal_id: str) -> Payment:
        client = self.client_repository.get(client_id)
        proposal = self.proposal_repository.get(client.id, proposal_id)

        self.proposal_repository.accept_proposal(client.id, proposal.id)
        payment = self._generate_payment_transaction(proposal)
        return self.payment_repository.create_payment(payment)

    def _generate_payment_transaction(self, proposal: Proposal) -> Payment:
        return Payment(
            proposal_id=proposal.id,
            amount=proposal.value,
            transaction_id=str(uuid4()),
            payment_date=timezone.now(),
        )
