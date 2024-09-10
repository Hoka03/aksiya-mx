from modeltranslation.translator import TranslationOptions, register

from .models import Wishlist


@register(Wishlist)
class WishlistTranslationOptions(TranslationOptions):
    fields = ("message",)