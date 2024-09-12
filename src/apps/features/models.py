from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from apps.categories.models import Category
from apps.general.normalize_text import normalize_text


class Feature(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    measure = models.CharField(max_length=20, blank=True, null=True)

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        unique_together = (('category', 'slug'),)

    def get_normalize_fields(self):
        return [
            'name',
            'slug'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class FeatureValue(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE,
                                related_name='feature_value')
    value = models.CharField(max_length=100)

    def get_normalize_fields(self):
        return [
            'value'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.value


class DiscountFeature(models.Model):
    discount = models.ForeignKey('discounts.Discount', on_delete=models.CASCADE,
                                 related_name='discount_features')
    feature_value = models.ForeignKey(FeatureValue, on_delete=models.CASCADE,
                                      related_name='product_feature')
    price = models.DecimalField(max_digits=20,
                                decimal_places=1,
                                default=0,
                                validators=[MinValueValidator(0)])
    ordering_number = models.PositiveSmallIntegerField()

    def clean(self):
        if self.discount.category_id != self.feature_value.feature.category_id:
            raise ValidationError("Feature value category does not match discount category")

    def __str__(self):
        return self.ordering_number