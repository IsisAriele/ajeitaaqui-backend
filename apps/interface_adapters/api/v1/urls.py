from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.interface_adapters.api.v1.views.create_client_view import CreateClientView
from apps.interface_adapters.api.v1.views.detail_client_view import DetailClientView
from apps.interface_adapters.api.v1.views.profile_client_view import ProfileClientView

urlpatterns = [
    path("register/", CreateClientView.as_view(), name="create-client"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("clients/<str:client_id>/", DetailClientView.as_view(), name="clients"),
    path("me/", ProfileClientView.as_view(), name="me"),
]
