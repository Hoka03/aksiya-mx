from modeltranslation.translator import TranslationOptions, register

from .models import Company, BranchCompany


@register(Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = ('last_name', 'first_name', 'father_name',
              'name', 'username', 'slogan', 'address',
              # 'description'
              )


@register(BranchCompany)
class BranchCompanyTranslationOptions(TranslationOptions):
    fields = ('name', 'address')
