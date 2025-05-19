from unittest.mock import Mock

from django.test import TestCase

from apps.domain.entities.client import Client
from apps.domain.exceptions.client_exceptions import ClientException
from apps.domain.interfaces.repositories.client_repository import ClientRepository
from apps.domain.usecases.detail_client_use_case import DetailClientUseCase


class TestDetailClientUseCase(TestCase):
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

    def test_should_call_repository_get_method(self):
        mock_repository = Mock(spec=ClientRepository)
        mock_repository.get.return_value = self.client

        use_case = DetailClientUseCase(mock_repository)

        client = use_case.get_client(self.client.id)

        mock_repository.get.assert_called_once_with(self.client.id)
        self.assertTrue(isinstance(client, Client))

    def test_should_raise_client_exception_on_repository_error(self):
        mock_repository = Mock(spec=ClientRepository)
        mock_repository.get.side_effect = Exception("Repository error")

        use_case = DetailClientUseCase(mock_repository)

        with self.assertRaises(ClientException) as context:
            use_case.get_client(self.client.id)

        self.assertEqual(str(context.exception), "Repository error")
