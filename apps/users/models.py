from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import IntegerChoices
from rest_framework.exceptions import ValidationError

from apps.users.managers import CustomUserManager
from apps.users.validations import phone_validate


class CustomUser(AbstractUser):
    class GenderChoices(IntegerChoices):
        MALE = 1, 'Male'
        FEMALE = 2, 'Female'

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    username = None
    objects = CustomUserManager()

    phone_number = models.CharField(max_length=13, validators=[phone_validate], unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=250)
    gender = models.PositiveSmallIntegerField(choices=GenderChoices.choices, default=1)
    balance = models.DecimalField(max_digits=10, decimal_places=1, default=0)

    def clean(self):
        if self.balance < 0:
            raise ValidationError('Balance must be bigger than 0.')

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'