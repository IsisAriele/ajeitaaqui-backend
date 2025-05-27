from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.infrastructure.models import ClientModel, CategoryModel, ServiceModel, PlanModel

admin.site.register(ClientModel, UserAdmin)
admin.site.register(CategoryModel)
admin.site.register(ServiceModel)
admin.site.register(PlanModel)

