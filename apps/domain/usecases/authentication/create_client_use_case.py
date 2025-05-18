from apps.domain.models.client_model import ClientModel
from django.db import IntegrityError
from django.core.exceptions import ValidationError


class CreateClientUseCase:
    def execute(self, validated_data: dict) -> ClientModel:
        client = ClientModel(
            username=validated_data["email"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            birth_date=validated_data.get("birth_date"),
            document=validated_data["document"],
            phone=validated_data["phone"],
            city=validated_data["city"],
            state=validated_data["state"],
            zip_code=validated_data["zip_code"],
            country=validated_data["country"],
            photo=validated_data.get("photo"),
        )

        client.set_password(validated_data["password"])

        try:
            client.full_clean()
            client.save()
        except (IntegrityError, ValidationError) as e:
            raise ValueError(f"Error creating client: {e}")

        return client
