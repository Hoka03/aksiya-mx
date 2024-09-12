from django.conf import settings
from django.db import models

from src.apps.companies.models import Company
from src.apps.general.normalize_text import normalize_text
from src.apps.users.validations import phone_validate


class Appeal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_normalize_fields(self):
        return [
            'message'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone_number
