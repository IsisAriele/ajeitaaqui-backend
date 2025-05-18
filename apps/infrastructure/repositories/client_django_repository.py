from apps.domain.entities.client import Client
from apps.infrastructure.models import ClientModel
from django.contrib.auth.hashers import make_password
from apps.domain.interfaces.repositories.client_repository import ClientRepository
from django.db import IntegrityError
from apps.domain.exceptions.client_exceptions import ClientException


class ClientDjangoRepository(ClientRepository):
    def create(self, client: Client) -> Client:
        try:
            ClientModel.objects.create(
                username=client.email,
                first_name=client.first_name,
                last_name=client.last_name,
                email=client.email,
                birth_date=client.birth_date,
                document=client.document,
                phone=client.phone,
                city=client.city,
                state=client.state,
                zip_code=client.zip_code,
                country=client.country,
                photo_url=client.photo_url,
                password=make_password(client.password) if client.password else None,
            )
        except IntegrityError:
            raise ClientException("E-mail/Document already registered.")

        return client
