from django.db import models

from apps.companies.choices import Country, District
from apps.general.normalize_text import normalize_text
from apps.users.validations import phone_validate


class BranchCompany(models.Model):
    company = models.ForeignKey('Company', on_delete=models.PROTECT)

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    address = models.CharField(max_length=255)

    country = models.PositiveSmallIntegerField(choices=Country.choices)
    district = models.PositiveSmallIntegerField(choices=District.choices)

    delivery = models.BooleanField(default=False)

    longitude = models.FloatField()
    latitude = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def get_normalize_fields(self):
        return [
            'name',
            'address'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def get_address(self):
        return {
            'address': self.address,
            'longitude': self.longitude,
            'latitude': self.latitude
        }

    def __str__(self):
        return self.name
