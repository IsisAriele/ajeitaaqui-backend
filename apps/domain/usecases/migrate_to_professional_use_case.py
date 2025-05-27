from apps.domain.entities.professional import Professional
from apps.domain.exceptions.professional_exceptions import ProfessionalException
from apps.domain.interfaces.repositories.professional_repository import ProfessionalRepository


class MigrateToProfessionalUseCase:
    def __init__(self, professional_repository: ProfessionalRepository):
        self.professional_repository = professional_repository

    def save_professional(self, client_id: str) -> Professional:
        try:
            return self.professional_repository.create(client_id)
        except Exception as e:
            raise ProfessionalException(str(e))
