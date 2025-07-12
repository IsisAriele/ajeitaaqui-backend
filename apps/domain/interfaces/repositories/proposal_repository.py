from abc import ABC, abstractmethod

from apps.domain.entities.proposal import Proposal


class ProposalRepository(ABC):
    @abstractmethod
    def create(self, proposal: Proposal) -> None:
        pass

    @abstractmethod
    def list_proposals_by_professional(self, professional_id: str):
        pass
