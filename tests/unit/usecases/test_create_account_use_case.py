from django.test import TestCase
from apps.domain.usecases.authentication.create_account_use_case import CreateAccountUseCase
from apps.domain.entities.client import Client
from apps.domain.interfaces.repositories.client_repository import ClientRepository
from unittest.mock import Mock
from apps.domain.exceptions.client_exceptions import ClientException


class TestCreateAccountUseCase(TestCase):
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

    def test_should_call_repository_create_method(self):
        mock_repository = Mock(spec=ClientRepository)
        use_case = CreateAccountUseCase(mock_repository)

        use_case.save_client(self.client)

        mock_repository.create.assert_called_once_with(self.client)

    def test_should_raise_client_exception_on_repository_error(self):
        mock_repository = Mock(spec=ClientRepository)
        mock_repository.create.side_effect = Exception("Repository error")

        use_case = CreateAccountUseCase(mock_repository)

        with self.assertRaises(ClientException) as context:
            use_case.save_client(self.client)

        self.assertEqual(str(context.exception), "Repository error")
