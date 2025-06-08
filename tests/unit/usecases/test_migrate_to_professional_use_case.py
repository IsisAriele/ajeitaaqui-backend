from unittest.mock import Mock

from django.test import TestCase

from apps.domain.exceptions.professional_exceptions import ProfessionalException
from apps.domain.interfaces.repositories.professional_repository import ProfessionalRepository
from apps.domain.usecases.migrate_to_professional_use_case import MigrateToProfessionalUseCase


class TestMigrateToProfessionalUseCase(TestCase):
    def setUp(self):
        self.client_id = "1"

    def test_should_call_repository_create_method(self):
        mock_repository = Mock(spec=ProfessionalRepository)
        use_case = MigrateToProfessionalUseCase(mock_repository)

        use_case.save_professional(self.client_id)

        mock_repository.create.assert_called_once_with(self.client_id)

    def test_should_raise_professional_exception_on_repository_error(self):
        mock_repository = Mock(spec=ProfessionalRepository)
        mock_repository.create.side_effect = Exception("Repository error")

        use_case = MigrateToProfessionalUseCase(mock_repository)

        with self.assertRaises(ProfessionalException) as context:
            use_case.save_professional(self.client_id)

        self.assertEqual(str(context.exception), "Repository error")
