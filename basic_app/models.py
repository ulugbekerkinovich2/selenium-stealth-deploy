from django.db import models


class UploadDatas(models.Model):
    link_for_get_data = models.URLField(max_length=300)
    login_for_that_site = models.CharField(max_length=50)
    password_for_that_site = models.CharField(max_length=50)
    link_for_upload_data2 = models.URLField(max_length=300)
    login_for_that_site2 = models.CharField(max_length=300)
    password_for_that_site2 = models.CharField(max_length=50)

    class Meta:
        db_table = 'upload_data'
        verbose_name_plural = 'upload_data'

    def __str__(self):
        return f"from {self.link_for_get_data} to {self.link_for_upload_data2}"
