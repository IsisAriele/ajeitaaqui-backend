from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.domain.exceptions.client_exceptions import ClientException
from apps.domain.usecases.create_client_use_case import CreateClientUseCase
from apps.infrastructure.repositories.django_client_repository import DjangoClientRepository
from apps.interface_adapters.api.v1.serializers.client_serializer import ClientSerializer


class CreateClientView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        client_entity = serializer.to_entity()
        client_repository = DjangoClientRepository()
        use_case = CreateClientUseCase(client_repository)

        try:
            use_case.save_client(client_entity)
        except ClientException as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_409_CONFLICT,
            )

        return Response(
            {"message": "Client created successfully"},
            status=status.HTTP_201_CREATED,
        )
