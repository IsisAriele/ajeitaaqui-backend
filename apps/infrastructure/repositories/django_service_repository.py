from apps.domain.entities.service import Service
from apps.domain.interfaces.repositories.service_repository import ServiceRepository
from apps.infrastructure.models.service_models import ServiceModel

class DjangoServiceRepository(ServiceRepository):
    def get_by_id(self, service_id: int) -> Service:
        try:
            service_model= ServiceModel.objects.get(id=service_id)
        except ServiceModel.DoesNotExist:
            raise Exception(f"Service with id {service_id} does not exist")
        
        return Service(
            id=service_model.id,
            description=service_model.description,
        )
