from abc import ABC, abstractmethod

from apps.domain.entities.professional import Professional


class ProfessionalRepository(ABC):
    @abstractmethod
    def create(self, client_id: str) -> Professional:
        pass

    @abstractmethod
    def get_by_id(self, client_id: str) -> Professional:
        pass
