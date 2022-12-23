from django.db.models.signals import post_save
from django.dispatch import receiver

from basic_app.models import UploadDatas


@receiver(post_save, sender=UploadDatas)
def selenium_uploads(sender, instance, **kwargs):
    selenium_uploads()
