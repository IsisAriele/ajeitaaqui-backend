from django.urls import path
from apps.interface_adapters.api.v1.views.authentication.create_client_view import ClientRegisterView

urlpatterns = [
    path("register/", ClientRegisterView.as_view(), name="client-register"),
]
