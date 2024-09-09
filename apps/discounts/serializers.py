from rest_framework import serializers
from ckeditor.fields import RichTextField

from .models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Discount
        fields = '__all__'

    def to_representation(self, instance):
        """Override to render content as CKEditor field in the API response."""
        data = super().to_representation(instance)
        # Example of modifying representation if needed
        data['content'] = RichTextField().to_python(instance.content)
        return data