from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     RetrieveAPIView)

from apps.companies.models.company import Company
from apps.companies.serializers.company import (CompanyListSerializer,
                                                CompanyCreateUpdateSerializer,
                                                CompanyRetrieveSerializer)


class CompanyListAPIView(ListAPIView):
    """
    Here we view Company ListAPIVIew
    """
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer


class CompanyCreateAPIVIew(CreateAPIView):
    """
    Here we view Company CreateAPIVIew
    """
    queryset = Company.objects.all()
    serializer_class = CompanyCreateUpdateSerializer


class CompanyUpdateAPIVIew(UpdateAPIView):
    """
    Here we view Company UpdateAPIVIew
    """
    queryset = Company.objects.all()
    serializer_class = CompanyCreateUpdateSerializer


class CompanyRetrieveAPIVIew(RetrieveAPIView):
    """
    Here we view only 1 object of Company model
    """
    queryset = Company.objects.all()
    serializer_class = CompanyRetrieveSerializer


class CompanyDestroyAPIVIew(DestroyAPIView):
    """
    Here we delete 1 objects of Company model
    """
    queryset = Company.objects.all()
