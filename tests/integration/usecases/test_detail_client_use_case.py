from django.test import TestCase

from apps.domain.entities.client import Client
from apps.domain.exceptions.client_exceptions import ClientException
from apps.domain.usecases.detail_client_use_case import DetailClientUseCase
from apps.infrastructure.models.user_models import ClientModel
from apps.infrastructure.repositories.django_client_repository import DjangoClientRepository


class TestDetailClientUseCase(TestCase):
    def setUp(self):
        self.client_model = ClientModel.objects.create(
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

    def test_should_return_client_details(self):
        client_repository = DjangoClientRepository()
        use_case = DetailClientUseCase(client_repository)
        client = use_case.get_client(self.client_model.id)
        self.assertIsInstance(client, Client)
        self.assertEqual(client.id, self.client_model.id)
        self.assertEqual(client.first_name, self.client_model.first_name)
        self.assertEqual(client.last_name, self.client_model.last_name)
        self.assertEqual(client.birth_date.strftime("%Y-%m-%d"), self.client_model.birth_date)
        self.assertEqual(client.document, self.client_model.document)
        self.assertEqual(client.email, self.client_model.email)
        self.assertEqual(client.phone, self.client_model.phone)
        self.assertEqual(client.city, self.client_model.city)
        self.assertEqual(client.state, self.client_model.state)
        self.assertEqual(client.zip_code, self.client_model.zip_code)
        self.assertEqual(client.country, self.client_model.country)

    def test_should_raise_client_exception_when_client_not_found(self):
        client_repository = DjangoClientRepository()
        use_case = DetailClientUseCase(client_repository)

        with self.assertRaises(ClientException) as context:
            use_case.get_client(0)

        self.assertEqual(str(context.exception), "ClientModel matching query does not exist.")
