from django.test import TestCase

from apps.domain.entities.client import Client
from apps.domain.exceptions.client_exceptions import ClientException
from apps.domain.usecases.update_client_use_case import UpdateClientUseCase
from apps.infrastructure.models.user_models import ClientModel
from apps.infrastructure.repositories.django_client_repository import DjangoClientRepository


class TestUpdateClientUseCase(TestCase):
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

        self.updated_client = Client(
            first_name="Novo Nome",
            last_name="Novo Sobrenome",
            birth_date="1999-11-30",
            document="xxx.xxx.xxx-yy",
            email="novonome@ifrn.com.br",
            phone="8199999-9999",
            city="Parnamirim",
            state="RN",
            zip_code="59000-123",
            country="BR",
            photo=None,
            password="123mudar",
        )

    def test_should_update_client_in_database(self):
        client_repository = DjangoClientRepository()
        use_case = UpdateClientUseCase(client_repository)
        use_case.update_client(client_id=self.client_model.id, client_updated=self.updated_client)
        update_client_model = ClientModel.objects.filter(
            id=1,
            first_name="Novo Nome",
            last_name="Novo Sobrenome",
            birth_date="1999-11-30",
            document="xxx.xxx.xxx-yy",
            email="novonome@ifrn.com.br",
            phone="8199999-9999",
            city="Parnamirim",
            state="RN",
            zip_code="59000-123",
            country="BR",
        ).first()

        self.assertIsNotNone(update_client_model)
        self.assertIsInstance(update_client_model, ClientModel)

    def test_should_raise_exception_when_client_does_not_exist(self):
        client_repository = DjangoClientRepository()
        use_case = UpdateClientUseCase(client_repository)

        with self.assertRaises(ClientException) as context:
            use_case.update_client(client_id="123", client_updated=self.updated_client)

        self.assertEqual(str(context.exception), "ClientModel matching query does not exist.")

    def test_should_raise_exception_when_update_data_is_invalid(self):
        client_repository = DjangoClientRepository()
        use_case = UpdateClientUseCase(client_repository)

        with self.assertRaises(ClientException) as context:
            use_case.update_client(
                client_id="1",
                client_updated=Client(
                    first_name=None,
                    last_name=None,
                    birth_date=None,
                    document=None,
                    email="naoehemail",
                    phone=None,
                    city=None,
                    state=None,
                    zip_code=None,
                    country=None,
                    photo=None,
                    password=None,
                ),
            )

        self.assertEqual(str(context.exception), "NOT NULL constraint failed: infrastructure_clientmodel.first_name")

    def test_should_raise_exception_when_email_is_not_unique(self):
        client_repository = DjangoClientRepository()
        use_case = UpdateClientUseCase(client_repository)

        new_client_model = ClientModel.objects.create(
            id="2",
            first_name="Ozzy",
            last_name="Osbourne",
            birth_date="1999-12-31",
            document="yyy.yyy.yyy-yy",
            email="ozzy@ifrn.com.br",
            username="ozzy@ifrn.com.br",
            phone="8499999-9998",
            city="Natal",
            state="RN",
            zip_code="59000-000",
            country="BR",
            photo=None,
            password="123mudar",
        )

        self.updated_client.email = new_client_model.email

        with self.assertRaises(ClientException) as context:
            use_case.update_client(client_id="1", client_updated=self.updated_client)

        self.assertEqual(str(context.exception), "UNIQUE constraint failed: infrastructure_clientmodel.username")

    def test_should_raise_exception_when_document_is_not_unique(self):
        client_repository = DjangoClientRepository()
        use_case = UpdateClientUseCase(client_repository)

        new_client_model = ClientModel.objects.create(
            id="2",
            first_name="Ozzy",
            last_name="Osbourne",
            birth_date="1999-12-31",
            document="yyy.yyy.yyy-yy",
            username="ozzy@ifrn.com.br",
            email="ozzy@ifrn.com.br",
            phone="8499999-9998",
            city="Natal",
            state="RN",
            zip_code="59000-000",
            country="BR",
            photo=None,
            password="123mudar",
        )

        self.updated_client.document = new_client_model.document

        with self.assertRaises(ClientException) as context:
            use_case.update_client(client_id="1", client_updated=self.updated_client)

        self.assertEqual(str(context.exception), "UNIQUE constraint failed: infrastructure_clientmodel.document")
