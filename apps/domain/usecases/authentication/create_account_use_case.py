from apps.domain.interfaces.repositories.client_repository import ClientRepository
from apps.domain.entities.client import Client
from apps.domain.exceptions.client_exceptions import ClientException


class CreateAccountUseCase:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def save_client(self, client: Client) -> Client:
        return self.client_repository.create(client)
