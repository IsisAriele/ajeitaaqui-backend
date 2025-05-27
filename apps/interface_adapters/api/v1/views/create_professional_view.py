from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.domain.exceptions.professional_exceptions import ProfessionalException
from apps.domain.usecases.migrate_to_professional_use_case import MigrateToProfessionalUseCase
from apps.infrastructure.repositories.django_professional_repository import DjangoProfessionalRepository


class CreateProfessionalView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        client_id = request.user.id

        repository = DjangoProfessionalRepository()
        use_case = MigrateToProfessionalUseCase(repository)

        try:
            use_case.save_professional(client_id)
        except ProfessionalException as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"message": "Professional created successfully"},
            status=status.HTTP_201_CREATED,
        )
