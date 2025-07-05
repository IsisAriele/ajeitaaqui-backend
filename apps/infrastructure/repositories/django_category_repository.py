from apps.domain.entities.category import Category
from apps.domain.interfaces.repositories.category_repository import CategoryRepository
from apps.infrastructure.models import CategoryModel


class DjangoCategoryRepository(CategoryRepository):
    def list_all(self):
        return [Category(id=cat.id, description=cat.description) for cat in CategoryModel.objects.all()]
