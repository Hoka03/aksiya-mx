from rest_framework import serializers

from .models import Discount, DiscountImage, ServiceDiscount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class DiscountImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountImage
        fields = '__all__'


class ServiceDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDiscount
        fields = '__all__'