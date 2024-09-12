from rest_framework import generics

from ..models import Feature
from ..serializers import FeatureSerializer


# List all features
class FeatureListAPIView(generics.ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


# Create a new feature
class FeatureCreateAPIView(generics.CreateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


# Retrieve a specific feature by ID
class FeatureRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


# Update a specific feature by ID
class FeatureUpdateAPIView(generics.UpdateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


# Delete a specific feature by ID
class FeatureDestroyAPIView(generics.DestroyAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
