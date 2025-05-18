from django.urls import path
from apps.interface_adapters.api.views.authentication.create_client_view import ClientCreateView

urlpatterns = [
    path("register/", ClientCreateView.as_view(), name="create-client"),
]
