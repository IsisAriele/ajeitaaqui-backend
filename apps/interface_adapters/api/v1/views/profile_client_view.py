from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.domain.usecases.update_client_use_case import UpdateClientUseCase
from apps.infrastructure.repositories.django_client_repository import DjangoClientRepository
from apps.interface_adapters.api.v1.serializers.client_serializer import ClientSerializer


class ProfileClientView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=ClientSerializer,
        responses={
            200: {"message": "Client updated successfully"},
            400: {"message": "Invalid data"},
            409: {"message": "Conflict"},
        },
    )
    def put(self, request):
        client_id = request.user.id
        serializer = ClientSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        client_entity = serializer.to_entity()
        client_repository = DjangoClientRepository()
        use_case = UpdateClientUseCase(client_repository)

        try:
            use_case.update_client(client_id, client_entity)
        except Exception as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_409_CONFLICT,
            )

        return Response(
            {"message": "Client updated successfully"},
            status=status.HTTP_200_OK,
        )
