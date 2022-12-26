from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from test1_automatic import selenium_upload




class UploadDatas(models.Model):
    # a = '/html/body/div[1]/div[2]'
    # b = '/div[2]/main/div[2]/div[1]/div'
    LEVEL_1 = '/html/body/div[1]/div[2]/div[2]/main/div[2]/div[1]/div'
    LEVEL_2 = '/html/body/div[1]/div[2]/div[2]/main/div[2]/div[2]/div'
    LEVEL_3 = '/html/body/div[1]/div[2]/div[2]/main/div[2]/div[3]/div'
    LEVEL_4 = '/html/body/div[1]/div[2]/div[2]/main/div[2]/div[4]/div'
    YEAR_IN_SCHOOL_CHOICES = [
        (LEVEL_1, 'LEVEL_1'),
        (LEVEL_2, 'LEVEL_2'),
        (LEVEL_3, 'LEVEL_3'),
        (LEVEL_4, 'LEVEL_4'),
    ]
    link_for_get_data = models.URLField(max_length=300, default='https://intranet.ytit.uz/course/view.php?id=3513')
    # login_for_that_site = models.CharField(max_length=50, default='ier20037')
    # password_for_that_site = models.CharField(max_length=50, default='AC2558243')
    link_for_upload_data2 = models.URLField(max_length=300, default='https://kiut.wisespace.uz/#/auth/login')
    login_for_that_site2 = models.CharField(max_length=300)
    password_for_that_site2 = models.CharField(max_length=50, default='password')
    input_your_folder_path = models.CharField(max_length=100, default='path kiritilmagan')
    input_level = models.CharField(choices=YEAR_IN_SCHOOL_CHOICES, max_length=100)
    name_of_course = models.CharField(max_length=70, default='course nomi kiritilmagan')
    wait_time = models.PositiveIntegerField(default='0', verbose_name='input_wait_time_when_upload_file in sekund')
    title = models.BooleanField(default=False, verbose_name='write title name to topic name')

    class Meta:
        db_table = 'upload_data'
        verbose_name_plural = 'upload_data'

    def __str__(self):
        return self.link_for_upload_data2


@receiver(post_save, sender=UploadDatas)
def selenium_uploads(sender, instance, *args, **kwargs):
    if instance.link_for_get_data:
        selenium_upload()
