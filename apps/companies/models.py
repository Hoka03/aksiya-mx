from django.conf import settings
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

from apps.categories.models import Category
from apps.companies.choices import Country, District
from apps.companies.validators import validate_company_video_size, validate_company_logo_size, \
    validate_company_banner_size
from apps.general.enums.week_days import WeekDay
from apps.users.validations import phone_validate


class Company(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    category = models.ManyToManyField(Category, blank=True)

    #   BIO FOR CREATE COMPANY ------ FIRST STEP
    last_name = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    father_name = models.CharField(max_length=120)

    #   CREATE COMPANY ------- SECOND STEP

    logo = models.ImageField(upload_to='company/logos/%Y/%m/%d/',
                             validators=[validate_company_logo_size],
                             blank=True, null=True)

    video = models.FileField(upload_to='company/videos/%Y/%m/%d/',
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['mp4']),
                                 validate_company_video_size, ],
                             blank=True, null=True)
    banner = models.ImageField(upload_to='company/banners/%Y/%m/%d/',
                               validators=[validate_company_banner_size],
                               blank=True, null=True)

    country = models.PositiveSmallIntegerField(choices=Country.choices)
    district = models.PositiveSmallIntegerField(choices=District.choices)

    name = models.CharField(max_length=250)
    username = models.SlugField(max_length=50, unique=True)
    slogan = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])

    id_generate = models.CharField(max_length=40, default='0')
    followers = models.CharField(max_length=40, default='0')
    likes = models.CharField(max_length=40, default='0')
    comments = models.CharField(max_length=40, default='0')
    views = models.CharField(max_length=50, default='0')

    delivery = models.BooleanField(default=False)
    installment = models.BooleanField(default=False)

    description = CKEditor5Field('content', config_name='extends')

    web_site = models.URLField(max_length=300)

    longitude = models.FloatField()
    latitude = models.FloatField()

    balance = models.DecimalField(max_digits=30, decimal_places=1, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    #   Rating fields
    rating5 = models.PositiveSmallIntegerField(default=0)
    rating4 = models.PositiveSmallIntegerField(default=0)
    rating3 = models.PositiveSmallIntegerField(default=0)
    rating2 = models.PositiveSmallIntegerField(default=0)
    rating1 = models.PositiveSmallIntegerField(default=0)

    def clean(self):
        cleaned_data = super().clean()
        country = cleaned_data.get('country')
        district = cleaned_data.get('district')

        # Define valid districts for each country
        country_districts = {
            Country.TASHKENT: [
                District.TASHKENT_CITY,
                District.YUNUSABAD,
                District.MIRABAD,
                District.CHILANZAR,
            ],
            Country.FERGANA: [
                District.FERGANA_CITY,
                District.KUVA,
                District.RISHTAN,
            ],
            Country.SAMARKAND: [
                District.SAMARKAND_CITY,
                District.URGUT,
                District.KATTALIK,
            ],
            Country.BUKHARA: [
                District.BUKHARA_CITY,
                District.JONDOR,
                District.GIDRO,
            ],
            Country.ANDIJAN: [
                District.ANDIJAN_CITY,
                District.ASAKA,
                District.KURGANTEPA,
            ],
            Country.NAVOI: [
                District.NAVOI_CITY,
                District.ZARAFSHAN,
                District.UCHKUDUK,
            ],
            Country.QARSHI: [
                District.QARSHI,
                District.KOSON,
                District.SHAKHRISABZ,
            ],
            Country.JIZZAKH: [
                District.JIZZAKH_CITY,
                District.PASTDARGOM,
                District.FORISH,
            ],
            Country.KHOREZM: [
                District.URGENCH,
                District.KHIVA,
                District.YANGIYER,
            ],
            Country.KOKAND: [
                District.KOKAND_CITY,
                District.RUSTAMYON,
                District.FAYZABAD,
            ],
            Country.TERMEZ: [
                District.TERMEZ_CITY,
                District.BOYSUN,
                District.SHERABAD,
            ],
        }

        if country in country_districts and district not in country_districts[country]:
            self.add_error('district', 'Selected district is not valid for the chosen country.')

        return cleaned_data


    def __str__(self):
        return self.name


class BranchCompany(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    address = models.CharField(max_length=255)

    delivery = models.BooleanField(default=False)

    longitude = models.FloatField()
    latitude = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CompanyTimeTable(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True, null=True)
    branch_company = models.ForeignKey(BranchCompany, on_delete=models.PROTECT, blank=True, null=True)

    week_day = models.PositiveSmallIntegerField(choices=WeekDay.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = (('company', 'week_day'),
                           ('branch_company', 'week_day'))

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError('start_time must be lower than end_time!')
