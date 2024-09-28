from rest_framework import serializers

from .models import Discount, DiscountImage, ServiceDiscount
from apps.companies.models.branch import BranchCompany


class DiscountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('company', 'branch_company', 'category', 'status',
                  'discount_type', 'currency', 'title', 'old_price',
                  'description', 'video', 'id_generate', 'in_stock',
                  'available', 'delivery', 'installment')


class DiscountCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Here checking CRUD for Discount Model
    """
    branch_company = serializers.PrimaryKeyRelatedField(queryset=BranchCompany.objects.all(),
        many=True, required=False)

    class Meta:
        model = Discount
        exclude = ('id_generate', 'views', 'comments', 'likes', 'dislikes')


    def create(self, validate_data):
        """
        Here Checking branch_company in create time, because it`s M2MField
        """
        branch_companies = validate_data.pop('branch_company', [])
        discount = Discount.objects.create(**validate_data)
        discount.branch_company.set(branch_companies)
        return discount


    def update(self, instance, validated_data):
        """
        Here Checking Update part
        """
        branch_companies = validated_data.pop('branch_company', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        instance.branch_company.set(branch_companies)
        return instance


    def validate(self, attrs):
        """
        Custom validation for model if required
        """
        model_clean = Discount(**attrs)
        model_clean.clean() # Custom Validation call
        return attrs


class DiscountRetrieveSerializer(serializers.ModelSerializer):
    """
    Here we are checking only 1 object. Type of Retrieve
    """
    class Meta:
        model = Discount
        """
        In Retrieve user does not see this fields
        """
        exclude = ('dislikes', 'discount_type', 'currency', 'is_active', 'created_at')



class DiscountImageSerializer(serializers.ModelSerializer):
    """
    Here Checking CRUD for DiscountImage Model
    """
    class Meta:
        model = DiscountImage
        fields = '__all__'



class ServiceDiscountSerializer(serializers.ModelSerializer):
    """
    Here Checking CRUD for ServiceDiscount Model
    """
    class Meta:
        model = ServiceDiscount
        fields = '__all__'

    def validate(self, attrs):
        """
        Custom validation for model if required
        """
        model_clean = ServiceDiscount(**attrs)
        model_clean.clean()
        return attrs