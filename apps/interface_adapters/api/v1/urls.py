from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.interface_adapters.api.v1.views.create_client_view import CreateClientView
from apps.interface_adapters.api.v1.views.create_professional_view import CreateProfessionalView
from apps.interface_adapters.api.v1.views.detail_client_view import DetailClientView
from apps.interface_adapters.api.v1.views.list_categories_views import ListCategoriesView
from apps.interface_adapters.api.v1.views.list_portfolios_view import ListPortfoliosView
from apps.interface_adapters.api.v1.views.manage_portfolio_views import ManagePortfolioViews
from apps.interface_adapters.api.v1.views.professional_proposals_views import ProfessionalProposalView
from apps.interface_adapters.api.v1.views.profile_client_view import ProfileClientView
from apps.interface_adapters.api.v1.views.search_portfolios_views import SearchPortfolioView

urlpatterns = [
    path("register/", CreateClientView.as_view(), name="create-client"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("clients/<str:client_id>/", DetailClientView.as_view(), name="clients"),
    path("me/", ProfileClientView.as_view(), name="me"),
    path("professional/", CreateProfessionalView.as_view(), name="create-professional"),
    path("professional/proposals/", ProfessionalProposalView.as_view(), name="professional-proposals"),
    path("manage/portfolios/", ManagePortfolioViews.as_view(), name="manage-portfolio"),
    path("portfolios/", ListPortfoliosView.as_view(), name="list-portfolios"),
    path("search/portfolios/", SearchPortfolioView.as_view(), name="search-portfolios"),
    path("categories/", ListCategoriesView.as_view(), name="list-categories"),
]
