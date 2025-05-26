from abc import ABC, abstractmethod

from apps.domain.entities.client import Client


class ClientRepository(ABC):
    @abstractmethod
    def create(self, client: Client) -> Client:
        pass

    @abstractmethod
    def get(self, client_id: str) -> Client:
        pass

    @abstractmethod
    def update(self, client_id: str, client_updated: Client) -> Client:
        pass
