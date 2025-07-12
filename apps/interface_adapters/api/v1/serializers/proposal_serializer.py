from rest_framework import serializers

from apps.domain.entities.professional import Client, Professional
from apps.domain.entities.proposal import Proposal


class SimpleClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100, read_only=True)
    last_name = serializers.CharField(max_length=100, read_only=True)


class SimplesServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=255, read_only=True)


class ListProposalsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    value = serializers.FloatField(read_only=True)
    scheduled_datetime = serializers.DateTimeField(read_only=True)
    client = SimpleClientSerializer(read_only=True)
    services = serializers.ListField(child=SimplesServiceSerializer(), read_only=True)
    confirmed = serializers.BooleanField(read_only=True)


class ProposalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    value = serializers.FloatField()
    scheduled_datetime = serializers.DateTimeField()
    client_id = serializers.IntegerField()
    professional_id = serializers.IntegerField()
    services = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    confirmed = serializers.BooleanField(default=False)

    def to_entity(self) -> Proposal:
        return Proposal(
            id=self.validated_data.get("id"),
            value=self.validated_data.get("value"),
            scheduled_datetime=self.validated_data.get("scheduled_datetime"),
            client=Client(
                id=self.validated_data.get("client_id"),
                first_name=None,
                last_name=None,
                birth_date=None,
                document=None,
                email=None,
                phone=None,
                city=None,
                state=None,
                zip_code=None,
                country=None,
            ),
            professional=Professional(
                id=self.validated_data.get("professional_id"),
                first_name=None,
                last_name=None,
                birth_date=None,
                document=None,
                email=None,
                phone=None,
                city=None,
                state=None,
                zip_code=None,
                country=None,
            ),
            services=self.validated_data.get("services", []),
            confirmed=self.validated_data.get("confirmed", False),
        )
