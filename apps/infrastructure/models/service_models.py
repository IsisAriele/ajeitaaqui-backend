from django.db import models


class CategoryModel(models.Model):
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="category_icons/", null=True, blank=True)

    def __str__(self):
        return self.description


class ServiceModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="services")
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
