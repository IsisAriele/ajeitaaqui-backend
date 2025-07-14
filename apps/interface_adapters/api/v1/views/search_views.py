from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.domain.usecases.search_use_case import SearchUseCase
from apps.infrastructure.repositories.django_portfolio_repository import DjangoPortfolioRepository
from apps.interface_adapters.api.v1.serializers.portfolio_serializer import PortfolioDetailSerializer


class SearchPortfolioView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="q", type=str, location=OpenApiParameter.QUERY, required=True, description="Texto da busca"
            ),
            OpenApiParameter(
                name="type",
                type=str,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Tipo da busca: 'service' ou 'professional'",
                enum=["service", "professional"],
            ),
        ],
        responses={
            200: PortfolioDetailSerializer(many=True),
            400: {"message": "Invalid data"},
        },
    )
    def get(self, request):
        query = request.query_params.get("q")
        search_type = request.query_params.get("type")  # 'service' ou 'professional'
        if not query or not search_type:
            raise ValidationError({"detail": "Parâmetros 'q' e 'type' são obrigatórios."})
        use_case = SearchUseCase(DjangoPortfolioRepository())
        if search_type == "service":
            portfolios = use_case.search_by_service(query)
        elif search_type == "professional":
            portfolios = use_case.search_by_professional(query)
        else:
            raise ValidationError({"detail": "O parâmetro 'type' deve ser 'service' ou 'professional'."})
        serializer = PortfolioDetailSerializer(portfolios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
