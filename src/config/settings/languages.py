from django.conf import settings


LANGUAGE_CODE = 'uz'

LANGUAGES = [
    ('uz', 'Uzbek'),
    ('ru', 'Russia'),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_LANGUAGE = ('uz', 'ru')


USE_I18N = True

LOCALE_PATHS = [
    settings.BASE_DIR / 'locale',
]
