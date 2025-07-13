from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.domain.usecases.reject_proposal_use_case import RejectProposalUseCase
from apps.infrastructure.repositories.django_client_repository import DjangoClientRepository
from apps.infrastructure.repositories.django_proposal_repository import DjangoProposalRepository


class ManageProposalsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, proposal_id):
        client_id = request.user.id
        proposal_repository = DjangoProposalRepository()
        client_repository = DjangoClientRepository()
        use_case = RejectProposalUseCase(proposal_repository, client_repository)

        try:
            use_case.reject(client_id, proposal_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
