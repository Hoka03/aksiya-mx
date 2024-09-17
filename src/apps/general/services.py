import os
from linecache import cache

from django.db.models import FileField, ImageField

from apps.general.tasks import get_currency


def delete_file_after_delete_obj(instance):
    for field in instance._meta.get_fields():
        if isinstance(field, (FileField, ImageField)):
            file_field = getattr(instance, field.name, None)
            if file_field and os.path.isfile(file_field.path):
                os.remove(file_field.path)


def get_usd_in_uzs():
    usd_and_sum = cache.get('usd_and_sum', None)
    if usd_and_sum is None:
        usd_and_sum = get_currency()
    return usd_and_sum

