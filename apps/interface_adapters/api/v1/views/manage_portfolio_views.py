from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.domain.usecases.manage_portfolio_use_case import ManagePortfolioUseCase
from apps.infrastructure.repositories.django_portfolio_repository import DjangoPortfolioRepository
from apps.infrastructure.repositories.django_professional_repository import DjangoProfessionalRepository
from apps.infrastructure.repositories.django_service_repository import DjangoServiceRepository
from apps.interface_adapters.api.v1.serializers.portfolio_serializer import PortfolioSerializer


class ManagePortfolioViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=PortfolioSerializer,
        responses={201: {"message": "Portfolio created successfully"}, 400: {"message": "Invalid data"}},
    )
    def post(self, request):
        client_id = request.user.id

        serializer = PortfolioSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        portfolio = serializer.to_entity(client_id)

        professional_repository = DjangoProfessionalRepository()
        portfolio_repository = DjangoPortfolioRepository()
        service_repository = DjangoServiceRepository()

        use_case = ManagePortfolioUseCase(professional_repository, portfolio_repository, service_repository)

        try:
            use_case.create_portfolio(portfolio)
        except Exception as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"message": "Portfolio created successfully"},
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        request=PortfolioSerializer,
        responses={200: {"message": "Portfolio updated successfully"}, 400: {"message": "Invalid data"}},
    )
    def put(self, request):
        client_id = request.user.id

        serializer = PortfolioSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        portfolio = serializer.to_entity(client_id)

        professional_repository = DjangoProfessionalRepository()
        portfolio_repository = DjangoPortfolioRepository()
        service_repository = DjangoServiceRepository()

        use_case = ManagePortfolioUseCase(professional_repository, portfolio_repository, service_repository)

        try:
            use_case.update_portfolio(portfolio)
        except Exception as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"message": "Portfolio updated successfully"},
            status=status.HTTP_200_OK,
        )
