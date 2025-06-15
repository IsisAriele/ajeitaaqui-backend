from abc import ABC, abstractmethod
from apps.domain.entities.service import Service

class ServiceRepository(ABC):
    @abstractmethod
    def get_by_id(self, service_id: str) -> Service:
        pass
