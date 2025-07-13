from rest_framework import serializers

from apps.domain.entities.portfolio import Portfolio
from apps.interface_adapters.api.v1.serializers.service_serializer import ServiceSerializer


class PortfolioSerializer(serializers.Serializer):
    description = serializers.CharField()
    image = serializers.ImageField(required=False, allow_null=True)
    services = serializers.ListField(child=serializers.IntegerField())

    def to_entity(self, client_id: int) -> Portfolio:
        return Portfolio(
            id=None,
            professional_id=client_id,
            description=self.validated_data.get("description"),
            image_url=self.validated_data.get("image"),
            services=self.validated_data.get("services"),
        )


class PortfolioDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    professional_id = serializers.IntegerField(read_only=True)
    description = serializers.CharField()
    image_url = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    services = ServiceSerializer(many=True)
