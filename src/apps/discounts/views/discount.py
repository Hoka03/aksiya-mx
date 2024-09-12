from rest_framework import generics

from ..serializers import DiscountSerializer
from ..models import Discount


# List all discounts
class DiscountListAPIView(generics.ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


# Create a new discount
class DiscountCreateAPIView(generics.CreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


# Retrieve a specific discount by ID
class DiscountRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


# Update a specific discount by ID
class DiscountUpdateAPIView(generics.UpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


# Delete a specific discount by ID
class DiscountDestroyAPIView(generics.DestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
