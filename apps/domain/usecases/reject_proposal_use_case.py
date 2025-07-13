from apps.domain.interfaces.repositories.client_repository import ClientRepository
from apps.domain.interfaces.repositories.proposal_repository import ProposalRepository


class RejectProposalUseCase:
    def __init__(self, proposal_repository: ProposalRepository, client_repository: ClientRepository):
        self.proposal_repository = proposal_repository
        self.client_repository = client_repository

    def reject(self, client_id: str, proposal_id: str):
        client = self.client_repository.get(client_id)
        self.proposal_repository.reject_proposal(client.id, proposal_id)
