from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.interface_adapters.api.v1.serializers.client_serializer import ClientSerializer
from apps.domain.usecases.authentication.create_client_use_case import CreateClientUseCase


class ClientRegisterView(APIView):
    def post(self, request):
        serializer = ClientSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        use_case = CreateClientUseCase()

        try:
            client = use_case.execute(serializer.validated_data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {"message": "Client created successfully!", "id": client.id, "username": client.username},
            status=status.HTTP_201_CREATED,
        )
