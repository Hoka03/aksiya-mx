from django.dispatch import receiver
from django.db.models.signals import post_delete

from apps.appeals.models import Appeal
from apps.general.services import delete_file_after_delete_obj


@receiver(post_delete, sender=Appeal)
def delete_photo_on_delete_user(instance, *args, **kwargs):
    delete_file_after_delete_obj(instance)
