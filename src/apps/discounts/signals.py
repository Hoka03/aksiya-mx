from django.dispatch import receiver
from django.db.models.signals import post_delete

from src.apps.discounts.models import Discount
from src.apps.general.services import delete_file_after_delete_obj


@receiver(post_delete, sender=Discount)
def delete_photo_on_delete_user(instance, *args, **kwargs):
    delete_file_after_delete_obj(instance)
