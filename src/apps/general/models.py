from django.db import models

from src.apps.discounts.choices import Currency


class CurrencyRate(models.Model):
    currency = models.PositiveSmallIntegerField(choices=Currency.choices)
    in_sum = models.DecimalField(max_digits=20, decimal_places=3, unique=True)
