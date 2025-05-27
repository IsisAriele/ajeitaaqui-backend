from apps.domain.entities.professional import Professional
from apps.domain.interfaces.repositories.professional_repository import ProfessionalRepository
from apps.infrastructure.models import ClientModel, ProfessionalModel


class DjangoProfessionalRepository(ProfessionalRepository):
    def create(self, client_id: str) -> Professional:
        try:
            client_model = ClientModel.objects.get(id=client_id)
        except ClientModel.DoesNotExist:
            raise Exception(f"Client with id {client_id} does not exist")

        try:
            professional_model = ProfessionalModel(client=client_model)
            professional_model.save()
        except Exception as e:
            raise Exception(f"Failed to create professional: {str(e)}")

        return Professional(
            first_name=professional_model.client.first_name,
            last_name=professional_model.client.last_name,
            birth_date=professional_model.client.birth_date,
            document=professional_model.client.document,
            email=professional_model.client.email,
            phone=professional_model.client.phone,
            city=professional_model.client.city,
            state=professional_model.client.state,
            zip_code=professional_model.client.zip_code,
            country=professional_model.client.country,
            photo=professional_model.client.photo,
            id=professional_model.id,
        )
