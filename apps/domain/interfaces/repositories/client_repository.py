from abc import ABC, abstractmethod
from apps.domain.entities.client import Client


class ClientRepository(ABC):
    @abstractmethod
    def create(self, client: Client) -> Client:
        pass
