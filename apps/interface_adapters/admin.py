from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.infrastructure.models import CategoryModel, ClientModel, PlanModel, ProfessionalModel, ServiceModel, PortfolioModel, PortfolioServiceModel

admin.site.register(ClientModel, UserAdmin)
admin.site.register(CategoryModel)
admin.site.register(ServiceModel)
admin.site.register(PlanModel)
admin.site.register(ProfessionalModel)
admin.site.register(PortfolioModel)
admin.site.register(PortfolioServiceModel)