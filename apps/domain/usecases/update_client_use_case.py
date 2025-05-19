from apps.domain.entities.client import Client
from apps.domain.exceptions.client_exceptions import ClientException
from apps.domain.interfaces.repositories.client_repository import ClientRepository


class UpdateClientUseCase:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def update_client(self, client_id: str, client_updated: Client) -> Client:
        try:
            return self.client_repository.update(client_id, client_updated)
        except Exception as e:
            raise ClientException(str(e))
