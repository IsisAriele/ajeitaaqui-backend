from apps.domain.entities.client import Client
from apps.domain.exceptions.client_exceptions import ClientException
from apps.domain.interfaces.repositories.client_repository import ClientRepository


class DetailClientUseCase:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def get_client(self, client_id: str) -> Client:
        try:
            return self.client_repository.get(client_id)
        except Exception as e:
            raise ClientException(str(e))
