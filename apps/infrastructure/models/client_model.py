from django.contrib.auth.models import AbstractUser
from django.db import models

# ✅ Para deixar claro: esses campos já existem no AbstractUser:
# username (vai ser o e-mail)
# first_name
# last_name
# email
# password
# is_active, is_staff, is_superuser
# date_joined, etc.


class ClientModel(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    document = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    photo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
