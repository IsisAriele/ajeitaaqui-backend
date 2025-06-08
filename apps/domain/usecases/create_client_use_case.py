from apps.domain.entities.client import Client
from apps.domain.exceptions.client_exceptions import ClientException
from apps.domain.interfaces.repositories.client_repository import ClientRepository


class CreateClientUseCase:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def save_client(self, client: Client) -> Client:
        try:
            return self.client_repository.create(client)
        except Exception as e:
            raise ClientException(str(e))
