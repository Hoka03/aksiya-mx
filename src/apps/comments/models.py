from django.conf import settings
from django.db import models

from src.apps.discounts.models import Discount
from src.apps.general.normalize_text import normalize_text


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null=True)
    discount = models.ForeignKey(Discount,
                                 on_delete=models.SET_NULL,
                                 null=True)
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_normalize_fields(self):
        return [
            'message'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.message