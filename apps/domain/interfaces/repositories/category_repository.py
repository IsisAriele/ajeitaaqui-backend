from abc import ABC, abstractmethod
from typing import List

from apps.domain.entities.category import Category


class CategoryRepository(ABC):
    @abstractmethod
    def list_all(self) -> List[Category]:
        pass
