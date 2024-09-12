from rest_framework import generics

from ..models import DiscountImage
from ..serializers import DiscountImageSerializer


# List all discount images
class DiscountImageListAPIView(generics.ListAPIView):
    queryset = DiscountImage.objects.all()
    serializer_class = DiscountImageSerializer


# Create a new discount image
class DiscountImageCreateAPIView(generics.CreateAPIView):
    queryset = DiscountImage.objects.all()
    serializer_class = DiscountImageSerializer


# Retrieve a specific discount image by ID
class DiscountImageRetrieveAPIView(generics.RetrieveAPIView):
    queryset = DiscountImage.objects.all()
    serializer_class = DiscountImageSerializer


# Update a specific discount image by ID
class DiscountImageUpdateAPIView(generics.UpdateAPIView):
    queryset = DiscountImage.objects.all()
    serializer_class = DiscountImageSerializer


# Delete a specific discount image by ID
class DiscountImageDestroyAPIView(generics.DestroyAPIView):
    queryset = DiscountImage.objects.all()
    serializer_class = DiscountImageSerializer
