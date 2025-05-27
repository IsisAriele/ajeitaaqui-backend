from django.db import models

from apps.infrastructure.models.user_models import ClientModel


class ProfessionalModel(models.Model):
    client = models.OneToOneField(ClientModel, on_delete=models.CASCADE, related_name="professional")

    def __str__(self):
        return f"Professional: {self.client}"
