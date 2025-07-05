from typing import List

from apps.domain.entities.category import Category
from apps.domain.interfaces.repositories.category_repository import CategoryRepository


class ListCategoriesUseCase:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def list_categories(self) -> List[Category]:
        return self.category_repository.list_all()
