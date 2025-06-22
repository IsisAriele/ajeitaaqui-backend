from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.domain.usecases.detail_portfolio_use_case import DetailPortfolioUseCase
from apps.infrastructure.repositories.django_portfolio_repository import DjangoPortfolioRepository
from apps.interface_adapters.api.v1.serializers.portfolio_serializer import PortfolioDetailSerializer


class DetailPortfolioView(APIView):
    def get(self, request, portfolio_id):
        portfolio_repository = DjangoPortfolioRepository()

        use_case = DetailPortfolioUseCase(portfolio_repository)

        try:
            portfolio = use_case.get_portfolio(portfolio_id)
        except Exception as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = PortfolioDetailSerializer.from_entity(portfolio)

        return Response(serializer.data, status=status.HTTP_200_OK)
