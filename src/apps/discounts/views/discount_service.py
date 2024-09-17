from rest_framework import generics

from ..models import ServiceDiscount
from ..serializers import ServiceDiscountSerializer


# List all service discounts
class ServiceDiscountListAPIView(generics.ListAPIView):
    queryset = ServiceDiscount.objects.all()
    serializer_class = ServiceDiscountSerializer


# Create a new service discount
class ServiceDiscountCreateAPIView(generics.CreateAPIView):
    queryset = ServiceDiscount.objects.all()
    serializer_class = ServiceDiscountSerializer


# Retrieve a specific service discount by ID
class ServiceDiscountRetrieveAPIView(generics.RetrieveAPIView):
    queryset = ServiceDiscount.objects.all()
    serializer_class = ServiceDiscountSerializer


# Update a specific service discount by ID
class ServiceDiscountUpdateAPIView(generics.UpdateAPIView):
    queryset = ServiceDiscount.objects.all()
    serializer_class = ServiceDiscountSerializer


# Delete a specific service discount by ID
class ServiceDiscountDestroyAPIView(generics.DestroyAPIView):
    queryset = ServiceDiscount.objects.all()
