from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.infrastructure.models import CategoryModel, ClientModel, PlanModel, ProfessionalModel, ServiceModel

admin.site.register(ClientModel, UserAdmin)
admin.site.register(CategoryModel)
admin.site.register(ServiceModel)
admin.site.register(PlanModel)
admin.site.register(ProfessionalModel)
