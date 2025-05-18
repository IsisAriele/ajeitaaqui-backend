from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.interface_adapters.api.serializers.client_serializer import ClientSerializer
from apps.domain.usecases.authentication.create_account_use_case import CreateAccountUseCase
from apps.infrastructure.repositories.client_django_repository import ClientDjangoRepository
from apps.domain.exceptions.client_exceptions import ClientException


class ClientCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)

        if serializer.is_valid():
            client_entity = serializer.to_entity()
            client_repository = ClientDjangoRepository()
            create_account_use_case = CreateAccountUseCase(client_repository)

            try:
                create_account_use_case.save_client(client_entity)
            except ClientException as e:
                return Response(
                    {"message": str(e)},
                    status=status.HTTP_409_CONFLICT,
                )

            return Response(
                {"message": "Cliente recebido com sucesso!", "client": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
