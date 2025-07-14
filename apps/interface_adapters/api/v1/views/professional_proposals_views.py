from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.domain.exceptions.proposal_exceptions import ProposalException
from apps.domain.usecases.create_proposal_use_case import CreateProposalUseCase
from apps.domain.usecases.list_professional_proposals_use_case import ListProfessionalProposalsUseCase
from apps.infrastructure.repositories.django_client_repository import DjangoClientRepository
from apps.infrastructure.repositories.django_professional_repository import DjangoProfessionalRepository
from apps.infrastructure.repositories.django_proposal_repository import DjangoProposalRepository
from apps.infrastructure.repositories.django_service_repository import DjangoServiceRepository
from apps.interface_adapters.api.v1.serializers.proposal_serializer import ListProposalsSerializer, ProposalSerializer


class ProfessionalProposalView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=ProposalSerializer,
        responses={201: {"message": "Proposal created successfully"}, 400: {"message": "Invalid data"}},
    )
    def post(self, request):
        request.data["professional_id"] = request.user.id
        serializer = ProposalSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        proposal_data = serializer.to_entity()

        use_case = CreateProposalUseCase(
            proposal_repository=DjangoProposalRepository(),
            client_repository=DjangoClientRepository(),
            professional_repository=DjangoProfessionalRepository(),
            service_repository=DjangoServiceRepository(),
        )
        try:
            use_case.create_proposal(proposal_data)
        except ProposalException as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(None, status=status.HTTP_201_CREATED)

    @extend_schema(
        request=None,
        responses={200: ListProposalsSerializer(many=True)},
    )
    def get(self, request):
        professional_id = request.user.id
        use_case = ListProfessionalProposalsUseCase(
            proposal_repository=DjangoProposalRepository(),
            professional_repository=DjangoProfessionalRepository(),
        )
        proposals = use_case.list_all(professional_id)

        serializer = ListProposalsSerializer(proposals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
