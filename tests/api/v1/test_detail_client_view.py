from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.infrastructure.models.user_models import ClientModel


class DetailClientViewTests(APITestCase):
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
        self.url = reverse("clients", args=[self.client_model.id])
        self.api_client.force_authenticate(user=self.client_model)

    def test_get_client_success(self):
        response = self.api_client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], self.client_model.first_name)
        self.assertEqual(response.data["last_name"], self.client_model.last_name)
        self.assertEqual(response.data["birth_date"], self.client_model.birth_date)
        self.assertEqual(response.data["document"], self.client_model.document)
        self.assertEqual(response.data["email"], self.client_model.email)
        self.assertEqual(response.data["phone"], self.client_model.phone)
        self.assertEqual(response.data["city"], self.client_model.city)
        self.assertEqual(response.data["state"], self.client_model.state)
        self.assertEqual(response.data["zip_code"], self.client_model.zip_code)
        self.assertEqual(response.data["country"], self.client_model.country)
        self.assertEqual(response.data["photo"], None)
