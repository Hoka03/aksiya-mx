from rest_framework import generics

from ..models import FeatureValue
from ..serializers import FeatureValueSerializer


# List all feature values
class FeatureValueListAPIView(generics.ListAPIView):
    queryset = FeatureValue.objects.all()
    serializer_class = FeatureValueSerializer


# Create a new feature value
class FeatureValueCreateAPIView(generics.CreateAPIView):
    queryset = FeatureValue.objects.all()
    serializer_class = FeatureValueSerializer


# Retrieve a specific feature value by ID
class FeatureValueRetrieveAPIView(generics.RetrieveAPIView):
    queryset = FeatureValue.objects.all()
    serializer_class = FeatureValueSerializer


# Update a specific feature value by ID
class FeatureValueUpdateAPIView(generics.UpdateAPIView):
    queryset = FeatureValue.objects.all()
    serializer_class = FeatureValueSerializer


# Delete a specific feature value by ID
class FeatureValueDestroyAPIView(generics.DestroyAPIView):
    queryset = FeatureValue.objects.all()
    serializer_class = FeatureValueSerializer
