from django.conf import settings
from django.db import models

from apps.discounts.models import Discount


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null=True)
    discount = models.ForeignKey(Discount,
                                 on_delete=models.SET_NULL,
                                 null=True)
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message