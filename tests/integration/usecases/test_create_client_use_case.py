from django.test import TestCase

from apps.domain.entities.client import Client
from apps.domain.exceptions.client_exceptions import ClientException
from apps.domain.usecases.create_client_use_case import CreateClientUseCase
from apps.infrastructure.models.user_models import ClientModel
from apps.infrastructure.repositories.django_client_repository import DjangoClientRepository


class TestCreateClientUseCase(TestCase):
    def setUp(self):
        self.client = Client(
            id="1",
            first_name="Nome",
            last_name="Sobrenome",
            birth_date="1999-12-31",
            document="xxx.xxx.xxx-xx",
            email="nome@ifrn.com.br",
            phone="8499999-9999",
            city="Natal",
            state="RN",
            zip_code="59000-000",
            country="BR",
            photo=None,
            password="123mudar",
        )

    def test_should_save_client_in_database(self):
        client_repository = DjangoClientRepository()
        use_case = CreateClientUseCase(client_repository)
        use_case.save_client(self.client)

        client_model = ClientModel.objects.get(email=self.client.email)

        self.assertEqual(client_model.first_name, self.client.first_name)
        self.assertEqual(client_model.last_name, self.client.last_name)
        self.assertEqual(client_model.birth_date.strftime("%Y-%m-%d"), self.client.birth_date)
        self.assertEqual(client_model.document, self.client.document)
        self.assertEqual(client_model.email, self.client.email)
        self.assertEqual(client_model.phone, self.client.phone)
        self.assertEqual(client_model.city, self.client.city)
        self.assertEqual(client_model.state, self.client.state)
        self.assertEqual(client_model.zip_code, self.client.zip_code)
        self.assertEqual(client_model.country, self.client.country)
        self.assertFalse(client_model.photo)

    def test_should_raise_client_exception_when_client_already_registered(self):
        client_repository = DjangoClientRepository()
        use_case = CreateClientUseCase(client_repository)
        use_case.save_client(self.client)

        with self.assertRaises(ClientException) as context:
            use_case.save_client(self.client)

        self.assertEqual(str(context.exception), "UNIQUE constraint failed: infrastructure_clientmodel.document")
