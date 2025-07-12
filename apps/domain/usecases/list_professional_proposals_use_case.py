from apps.domain.interfaces.repositories.professional_repository import ProfessionalRepository
from apps.domain.interfaces.repositories.proposal_repository import ProposalRepository


class ListProfessionalProposalsUseCase:
    def __init__(self, proposal_repository: ProposalRepository, professional_repository: ProfessionalRepository):
        self.proposal_repository = proposal_repository
        self.professional_repository = professional_repository

    def list_all(self, client_id: str):
        professional = self.professional_repository.get_by_id(client_id)
        return self.proposal_repository.list_proposals_by_professional(professional.id)
