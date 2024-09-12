from modeltranslation.translator import TranslationOptions, register

from src.apps.advertisements.models import Advertisement

@register(Advertisement)
class AdvertisementTranslationOptions(TranslationOptions):
    fields = ('title', 'slug')