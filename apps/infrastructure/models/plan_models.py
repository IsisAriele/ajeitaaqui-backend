from django.db import models


class PlanModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
