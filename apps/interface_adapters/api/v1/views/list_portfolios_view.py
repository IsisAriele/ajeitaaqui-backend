from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.domain.usecases.list_portfolios_use_case import ListPortfoliosUseCase
from apps.infrastructure.repositories.django_portfolio_repository import DjangoPortfolioRepository
from apps.interface_adapters.api.v1.serializers.portfolio_serializer import PortfolioDetailSerializer


class ListPortfoliosView(APIView):
    @extend_schema(
        request=None,
        responses={200: PortfolioDetailSerializer},
    )
    def get(self, request):
        use_case = ListPortfoliosUseCase(DjangoPortfolioRepository())
        portfolios = use_case.list_portfolios()
        serializer = PortfolioDetailSerializer(portfolios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
