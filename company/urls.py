# region				----- External Imports -----
from django.urls import path
# endregion

# region				----- Internal Imports -----
from .views import HomeView, CompanyDetailView, CreateCompanyView
# endregion

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    path('create/', CreateCompanyView.as_view(), name='create_company'),
]