from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.domain.usecases.list_client_proposals_use_case import ListClientProposalsUseCase
from apps.infrastructure.repositories.django_client_repository import DjangoClientRepository
from apps.infrastructure.repositories.django_proposal_repository import DjangoProposalRepository
from apps.interface_adapters.api.v1.serializers.proposal_serializer import ListProposalsSerializer


class ListClientProposalsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(parameters=None, responses={200: ListProposalsSerializer(many=True)})
    def get(self, request):
        client_id = request.user.id
        proposal_repository = DjangoProposalRepository()
        client_repository = DjangoClientRepository()
        use_case = ListClientProposalsUseCase(proposal_repository, client_repository)
        proposals = use_case.list_all(client_id)
        serializer = ListProposalsSerializer(proposals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
