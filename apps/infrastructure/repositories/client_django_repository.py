from django.contrib.auth.hashers import make_password

from apps.domain.entities.client import Client
from apps.domain.interfaces.repositories.client_repository import ClientRepository
from apps.infrastructure.models import ClientModel


class DjangoClientRepository(ClientRepository):
    def create(self, client: Client) -> Client:
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
            photo=client.photo,
            password=make_password(client.password) if client.password else None,
        )
        return client

    def get(self, client_id: str) -> Client:
        client_model = ClientModel.objects.get(id=client_id)
        return Client(
            id=client_model.id,
            first_name=client_model.first_name,
            last_name=client_model.last_name,
            email=client_model.email,
            birth_date=client_model.birth_date,
            document=client_model.document,
            phone=client_model.phone,
            city=client_model.city,
            state=client_model.state,
            zip_code=client_model.zip_code,
            country=client_model.country,
            photo=client_model.photo,
        )

    def update(self, client_id: str, client_updated: Client) -> Client:
        client_model = ClientModel.objects.get(id=client_id)

        client_model.first_name = client_updated.first_name
        client_model.last_name = client_updated.last_name
        client_model.email = client_updated.email
        client_model.username = client_updated.email
        client_model.birth_date = client_updated.birth_date
        client_model.document = client_updated.document
        client_model.phone = client_updated.phone
        client_model.city = client_updated.city
        client_model.state = client_updated.state
        client_model.zip_code = client_updated.zip_code
        client_model.country = client_updated.country
        client_model.photo = client_updated.photo

        if client_updated.password:
            client_model.password = make_password(client_updated.password)

        client_model.save()

        return Client(
            id=client_model.id,
            first_name=client_model.first_name,
            last_name=client_model.last_name,
            email=client_model.email,
            birth_date=client_model.birth_date,
            document=client_model.document,
            phone=client_model.phone,
            city=client_model.city,
            state=client_model.state,
            zip_code=client_model.zip_code,
            country=client_model.country,
            photo=client_model.photo,
        )
