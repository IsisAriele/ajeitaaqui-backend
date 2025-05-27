from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.infrastructure.models.user_models import ClientModel


class ProfileClientViewTests(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
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

        self.api_client.force_authenticate(user=self.client_model)
        self.url = reverse("me")

        self.valid_payload = {
            "first_name": "João",
            "last_name": "Silva",
            "birth_date": "1990-01-01",
            "document": "12345678900",
            "email": "joao@example.com",
            "phone": "11999999999",
            "city": "São Paulo",
            "state": "SP",
            "zip_code": "01000-000",
            "country": "Brasil",
            "password": "strongpassword123",
        }

    def test_update_client_success(self):
        response = self.api_client.put(self.url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Client updated successfully")

    def test_create_client_invalid_payload(self):
        payload = {}

        response = self.api_client.put(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)
        self.assertIn("document", response.data)
        self.assertIn("first_name", response.data)
        self.assertIn("last_name", response.data)
        self.assertIn("birth_date", response.data)
        self.assertIn("phone", response.data)
        self.assertIn("city", response.data)
        self.assertIn("state", response.data)
        self.assertIn("zip_code", response.data)
        self.assertIn("country", response.data)
        self.assertIn("password", response.data)

    def test_create_client_duplicate_document(self):
        new_client_model = ClientModel.objects.create(
            first_name="Novo Nome",
            last_name="Novo Sobrenome",
            birth_date="1999-12-30",
            document="yyy.yyy.yyy-yy",
            email="novo@ifrn.com.br",
            username="novo@ifrn.com.br",
            phone="8499999-9998",
            city="Natal",
            state="RN",
            zip_code="59000-000",
            country="BR",
            photo=None,
            password="123mudar",
        )

        payload = self.valid_payload.copy()
        payload["document"] = new_client_model.document

        response = self.api_client.put(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertIn("message", response.data)

    def test_create_client_duplicate_email(self):
        new_client_model = ClientModel.objects.create(
            first_name="Novo Nome",
            last_name="Novo Sobrenome",
            birth_date="1999-12-30",
            document="yyy.yyy.yyy-yy",
            username="novo@ifrn.com.br",
            email="novo@ifrn.com.br",
            phone="8499999-9998",
            city="Natal",
            state="RN",
            zip_code="59000-000",
            country="BR",
            photo=None,
            password="123mudar",
        )

        payload = self.valid_payload.copy()
        payload["email"] = new_client_model.email

        response = self.api_client.put(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertIn("message", response.data)
