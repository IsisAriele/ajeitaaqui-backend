from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.domain.usecases.detail_client_use_case import DetailClientUseCase
from apps.infrastructure.repositories.django_client_repository import DjangoClientRepository
from apps.interface_adapters.api.v1.serializers.client_serializer import ClientSerializer


class DetailClientView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=None,
        responses={200: ClientSerializer, 404: {"message": "Not found"}},
    )
    def get(self, request, client_id):
        client_repository = DjangoClientRepository()
        use_case = DetailClientUseCase(client_repository)

        try:
            client = use_case.get_client(client_id)
        except Exception as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)
