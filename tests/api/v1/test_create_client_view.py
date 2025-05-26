from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class CreateClientViewTests(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.url = reverse("create-client")
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

    def test_create_client_success(self):
        response = self.api_client.post(self.url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Client created successfully")

    def test_create_client_invalid_payload(self):
        payload = {}

        response = self.api_client.post(self.url, payload, format="json")
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
        self.api_client.post(self.url, self.valid_payload, format="json")

        payload = self.valid_payload.copy()
        payload["email"] = "novo@example.com"

        response = self.api_client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertIn("message", response.data)

    def test_create_client_duplicate_email(self):
        self.api_client.post(self.url, self.valid_payload, format="json")

        payload = self.valid_payload.copy()
        payload["document"] = "98765432100"

        response = self.api_client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertIn("message", response.data)
