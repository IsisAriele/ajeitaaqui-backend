from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.infrastructure.models.user_models import ClientModel


class CreateProfessionalViewTests(APITestCase):
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
        self.url = reverse("create-professional")
        self.api_client.force_authenticate(user=self.client_model)

    def test_create_professional_success(self):
        response = self.api_client.post(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_professional_already_exists(self):
        response = self.api_client.post(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.api_client.post(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("message", response.data)
        self.assertEqual(
            response.data["message"],
            "Failed to create professional: UNIQUE constraint failed: infrastructure_professionalmodel.client_id",
        )
