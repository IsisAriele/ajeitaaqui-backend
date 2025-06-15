from rest_framework import serializers

from apps.domain.entities.portfolio import Portfolio
from apps.domain.entities.professional import Professional

class PortfolioSerializer(serializers.Serializer):
    description = serializers.CharField()
    image = serializers.ImageField(required=False, allow_null=True)
    services = serializers.ListField(child=serializers.IntegerField())

    def to_entity(self, client_id: int) -> Portfolio:
        return Portfolio(
            id=None,
            professional_id=client_id,
            description=self.validated_data.get('description'),
            image_url=self.validated_data.get('image'),
            services=self.validated_data.get('services'),
        )
