from apps.domain.entities.proposal import Proposal
from apps.domain.interfaces.repositories.proposal_repository import ProposalRepository
from apps.infrastructure.models import ProposalModel, ProposalServiceModel


class DjangoProposalRepository(ProposalRepository):
    def create(self, proposal: Proposal) -> Proposal:
        proposal_model = ProposalModel.objects.create(
            confirmed=proposal.confirmed,
            value=proposal.value,
            scheduled_datetime=proposal.scheduled_datetime,
            client_id=proposal.client.id,
            professional_id=proposal.professional.id,
        )

        for service in proposal.services:
            ProposalServiceModel.objects.create(proposal=proposal_model, service_id=service.id)

        return Proposal(
            id=proposal_model.id,
            confirmed=proposal_model.confirmed,
            value=proposal_model.value,
            scheduled_datetime=proposal_model.scheduled_datetime,
            client=proposal.client,
            professional=proposal.professional,
            services=[service for service in proposal.services],
        )
