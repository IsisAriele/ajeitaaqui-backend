from rest_framework import serializers

from apps.domain.entities.service import Service


class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField()

    def to_entity(self) -> Service:
        return Service(
            id=self.validated_data.get("id"),
            description=self.validated_data.get("description"),
        )
