from rest_framework import generics

from ..models import DiscountFeature
from ..serializers import DiscountFeatureSerializer


# List all discount features
class DiscountFeatureListAPIView(generics.ListAPIView):
    queryset = DiscountFeature.objects.all()
    serializer_class = DiscountFeatureSerializer


# Create a new discount feature
class DiscountFeatureCreateAPIView(generics.CreateAPIView):
    queryset = DiscountFeature.objects.all()
    serializer_class = DiscountFeatureSerializer


# Retrieve a specific discount feature by ID
class DiscountFeatureRetrieveAPIView(generics.RetrieveAPIView):
    queryset = DiscountFeature.objects.all()
    serializer_class = DiscountFeatureSerializer


# Update a specific discount feature by ID
class DiscountFeatureUpdateAPIView(generics.UpdateAPIView):
    queryset = DiscountFeature.objects.all()
    serializer_class = DiscountFeatureSerializer


# Delete a specific discount feature by ID
class DiscountFeatureDestroyAPIView(generics.DestroyAPIView):
    queryset = DiscountFeature.objects.all()
    serializer_class = DiscountFeatureSerializer
