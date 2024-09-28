from modeltranslation.translator import TranslationOptions, register

from apps.companies.models.company import Company
from apps.companies.models.branch import BranchCompany


@register(Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = ('last_name', 'first_name', 'father_name',
              'name', 'username', 'slogan', 'address', 'description')


@register(BranchCompany)
class BranchCompanyTranslationOptions(TranslationOptions):
    fields = ('name', 'address')
