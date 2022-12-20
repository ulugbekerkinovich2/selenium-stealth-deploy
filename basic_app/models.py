from django.db import models

from test1_automatic import selenium_upload


class UploadDatas(models.Model):
    link_for_get_data = models.URLField(max_length=300)
    login_for_that_site = models.CharField(max_length=50)
    password_for_that_site = models.CharField(max_length=50)
    link_for_upload_data2 = models.URLField(max_length=300)
    login_for_that_site2 = models.CharField(max_length=300)
    password_for_that_site2 = models.CharField(max_length=50)
    input_your_folder_path = models.CharField(max_length=100, default='path kiritilmagan')

    class Meta:
        db_table = 'upload_data'
        verbose_name_plural = 'upload_data'

    # def __str__(self):
    #     return selenium_upload()

