from django.test import TestCase

from apps.domain.usecases.migrate_to_professional_use_case import MigrateToProfessionalUseCase
from apps.infrastructure.models.professional_models import ProfessionalModel
from apps.infrastructure.models.user_models import ClientModel
from apps.infrastructure.repositories.django_professional_repository import DjangoProfessionalRepository


class TestMigrateToProfessionalUseCase(TestCase):
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

    def test_should_migrate_client_to_professional(self):
        professional_repository = DjangoProfessionalRepository()
        use_case = MigrateToProfessionalUseCase(professional_repository)

        use_case.save_professional(self.client_model.id)
        professional = ProfessionalModel.objects.get(client_id=self.client_model.id)
        self.assertEqual(professional.client_id, self.client_model.id)

    def test_should_raise_exception_when_client_not_found(self):
        professional_repository = DjangoProfessionalRepository()
        use_case = MigrateToProfessionalUseCase(professional_repository)

        with self.assertRaises(Exception) as context:
            use_case.save_professional("0")

        self.assertEqual(str(context.exception), "Client with id 0 does not exist")

    def test_should_raise_exception_when_professional_already_exists(self):
        professional_repository = DjangoProfessionalRepository()
        use_case = MigrateToProfessionalUseCase(professional_repository)

        # First migration
        use_case.save_professional(self.client_model.id)

        # Second migration should raise an exception
        with self.assertRaises(Exception) as context:
            use_case.save_professional(self.client_model.id)

        self.assertEqual(
            str(context.exception),
            "Failed to create professional: UNIQUE constraint failed: infrastructure_professionalmodel.client_id",
        )
