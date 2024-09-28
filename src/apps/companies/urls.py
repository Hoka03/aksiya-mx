from django.urls import path

from apps.companies.views.company import (CompanyListAPIView, CompanyCreateAPIVIew,
                                          CompanyUpdateAPIVIew, CompanyDestroyAPIVIew,
                                          CompanyRetrieveAPIVIew)

urlpatterns = [
    #   HERE URLS OF COMPANY MODEL
    path('company-list/', CompanyListAPIView.as_view(), name='company-list'),
    path('company-create/', CompanyCreateAPIVIew.as_view(), name='company-create'),
    path('company-update/', CompanyUpdateAPIVIew.as_view(), name='company-update'),
    path('company-delete/', CompanyDestroyAPIVIew.as_view(), name='company-delete'),
    path('company-delete/', CompanyRetrieveAPIVIew.as_view(), name='company-retrieve'),
]