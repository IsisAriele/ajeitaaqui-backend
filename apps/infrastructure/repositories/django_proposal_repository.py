from apps.domain.entities.proposal import Proposal
from apps.domain.interfaces.repositories.proposal_repository import ProposalRepository
from apps.infrastructure.models import ProposalModel, ProposalServiceModel


class DjangoProposalRepository(ProposalRepository):
    def list_proposals_by_client(self, client_id: str):
        proposals = list()
        proposal_models = ProposalModel.objects.filter(client_id=client_id)

        for proposal_model in proposal_models:
            services = [service.service for service in proposal_model.proposal_services.all()]
            proposal = Proposal(
                id=proposal_model.id,
                confirmed=proposal_model.confirmed,
                value=proposal_model.value,
                scheduled_datetime=proposal_model.scheduled_datetime,
                client=proposal_model.client,
                professional=proposal_model.professional,
                services=services,
            )
            proposals.append(proposal)

        return proposals

    def list_proposals_by_professional(self, professional_id: str):
        proposals = list()
        proposal_models = ProposalModel.objects.filter(professional_id=professional_id)

        for proposal_model in proposal_models:
            services = [service.service for service in proposal_model.proposal_services.all()]
            proposal = Proposal(
                id=proposal_model.id,
                confirmed=proposal_model.confirmed,
                value=proposal_model.value,
                scheduled_datetime=proposal_model.scheduled_datetime,
                client=proposal_model.client,
                professional=proposal_model.professional,
                services=services,
            )
            proposals.append(proposal)

        return proposals

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
