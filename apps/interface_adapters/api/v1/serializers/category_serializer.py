from rest_framework import serializers

from apps.domain.entities.category import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField()

    def to_entity(self) -> Category:
        return Category(
            id=self.validated_data.get("id"),
            description=self.validated_data.get("description"),
        )
