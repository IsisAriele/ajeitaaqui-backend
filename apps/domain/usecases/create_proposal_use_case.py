from apps.domain.entities.proposal import Proposal
from apps.domain.exceptions.proposal_exceptions import ProposalException
from apps.domain.interfaces.repositories.client_repository import ClientRepository
from apps.domain.interfaces.repositories.professional_repository import ProfessionalRepository
from apps.domain.interfaces.repositories.proposal_repository import ProposalRepository
from apps.domain.interfaces.repositories.service_repository import ServiceRepository


class CreateProposalUseCase:
    def __init__(
        self,
        proposal_repository: ProposalRepository,
        client_repository: ClientRepository,
        professional_repository: ProfessionalRepository,
        service_repository: ServiceRepository,
    ):
        self.proposal_repository = proposal_repository
        self.client_repository = client_repository
        self.professional_repository = professional_repository
        self.service_repository = service_repository

    def create_proposal(
        self,
        proposal: Proposal,
    ) -> Proposal:
        try:
            proposal.client = self.client_repository.get(proposal.client.id)
            proposal.professional = self.professional_repository.get_by_id(proposal.professional.id)
            proposal.services = [self.service_repository.get_by_id(service_id) for service_id in proposal.services]
            return self.proposal_repository.create(proposal)
        except Exception as e:
            raise ProposalException(f"Erro ao criar proposta: {str(e)}")
