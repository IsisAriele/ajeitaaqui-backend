from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.domain.usecases.list_categories_use_case import ListCategoriesUseCase
from apps.infrastructure.repositories.django_category_repository import DjangoCategoryRepository
from apps.interface_adapters.api.v1.serializers.category_serializer import CategorySerializer


class ListCategoriesView(APIView):
    def get(self, request):
        use_case = ListCategoriesUseCase(DjangoCategoryRepository())
        categories = use_case.list_categories()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
