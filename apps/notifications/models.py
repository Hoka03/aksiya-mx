from django.db import models
from django.db.models import SET_NULL

from apps.companies.models import Company, BranchCompany
from apps.discounts.choices import DiscountChoices


class Notification(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL,
                                null=True)
    branch_company = models.ForeignKey(BranchCompany, on_delete=SET_NULL,
                                       null=True)
    old_price = models.DecimalField(max_digits=20, decimal_places=1, default=0)
    discount = models.PositiveSmallIntegerField(choices=DiscountChoices.choices)
    discount_counts = models.PositiveSmallIntegerField()
    remaining_discounts = models.PositiveSmallIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    tags = models.CharField(max_length=20)
    title = models.CharField(max_length=150)
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title