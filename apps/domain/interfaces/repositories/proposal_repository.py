from abc import ABC, abstractmethod

from apps.domain.entities.proposal import Proposal


class ProposalRepository(ABC):
    @abstractmethod
    def create(self, proposal: Proposal) -> None:
        pass

    @abstractmethod
    def get(self, client_id: str, proposal_id: str) -> Proposal:
        pass

    @abstractmethod
    def list_proposals_by_professional(self, professional_id: str):
        pass

    @abstractmethod
    def list_proposals_by_client(self, client_id: str):
        pass

    @abstractmethod
    def reject_proposal(self, client_id: str, proposal_id: str) -> None:
        pass

    @abstractmethod
    def accept_proposal(self, client_id: str, proposal_id: str) -> None:
        pass
