from django.conf import settings
from django.db import models

from apps.companies.models import Company
from apps.users.validations import phone_validate


class Appeal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number