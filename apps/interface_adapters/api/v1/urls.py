from django.urls import path
from apps.interface_adapters.api.v1.views.authentication.create_client_view import ClientCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", ClientCreateView.as_view(), name="create-client"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
