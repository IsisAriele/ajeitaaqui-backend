from apps.domain.interfaces.repositories.client_repository import ClientRepository
from apps.domain.interfaces.repositories.proposal_repository import ProposalRepository


class ListClientProposalsUseCase:
    def __init__(self, proposal_repository: ProposalRepository, client_repository: ClientRepository):
        self.proposal_repository = proposal_repository
        self.client_repository = client_repository

    def list_all(self, client_id: str):
        client = self.client_repository.get(client_id)
        return self.proposal_repository.list_proposals_by_client(client.id)
