from rest_framework import serializers
from apps.domain.entities.client import Client


class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birth_date = serializers.DateField()
    document = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    zip_code = serializers.CharField()
    country = serializers.CharField()
    photo_url = serializers.URLField(required=False, allow_blank=True)
    password = serializers.CharField()

    def to_entity(self) -> Client:
        """Converte os dados validados em uma instância da entidade Client"""
        return Client(**self.validated_data)
