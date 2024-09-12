from django.dispatch import receiver
from django.db.models.signals import post_delete

from apps.categories.models import Category
from apps.general.services import delete_file_after_delete_obj


@receiver(post_delete, sender=Category)
def delete_photo_on_delete_user(instance, *args, **kwargs):
    delete_file_after_delete_obj(instance)
