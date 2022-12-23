from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from test1_automatic import selenium_upload


class Mylevel(models.Model):
    level = models.CharField(max_length=200, default='berilmagan course XPATH')

    class Meta:
        db_table = 'mylevel'
        verbose_name_plural = 'mylevel'

    def __str__(self):
        return f"{self.level}"


class UploadDatas(models.Model):
    link_for_get_data = models.URLField(max_length=300, default='https://intranet.ytit.uz/course/view.php?id=3577')
    login_for_that_site = models.CharField(max_length=50, default='ier20037')
    password_for_that_site = models.CharField(max_length=50, default='AC2558243')
    link_for_upload_data2 = models.URLField(max_length=300, default='https://lms.spprt.uz/#/auth/login')
    login_for_that_site2 = models.CharField(max_length=300)
    password_for_that_site2 = models.CharField(max_length=50, default='password')
    input_your_folder_path = models.CharField(max_length=100, default='path kiritilmagan')
    input_level_of_XPATH = models.ForeignKey(Mylevel, on_delete=models.CASCADE)
    name_of_course = models.CharField(max_length=70, default='course nomi kiritilmagan')

    class Meta:
        db_table = 'upload_data'
        verbose_name_plural = 'upload_data'

    def __str__(self):
        return self.link_for_upload_data2


@receiver(post_save, sender=UploadDatas)
def selenium_uploads(sender, instance, *args, **kwargs):
    if instance.link_for_get_data:
        selenium_upload()
