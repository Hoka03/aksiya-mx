from rest_framework import generics

from ..serializers import DiscountCreateUpdateSerializer, DiscountRetrieveSerializer, DiscountListSerializer
from ..models import Discount


# List all discounts
class DiscountListAPIView(generics.ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountListSerializer


# Create a new discount
class DiscountCreateAPIView(generics.CreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountCreateUpdateSerializer


# Retrieve a specific discount by ID
class DiscountRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountRetrieveSerializer


# Update a specific discount by ID
class DiscountUpdateAPIView(generics.UpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountCreateUpdateSerializer


# Delete a specific discount by ID
class DiscountDestroyAPIView(generics.DestroyAPIView):
    queryset = Discount.objects.all()
