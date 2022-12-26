# Generated by Django 4.1.2 on 2022-12-25 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0023_alter_uploaddatas_link_for_get_data_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploaddatas',
            name='input_wait_time_when_upload_file',
        ),
        migrations.AddField(
            model_name='uploaddatas',
            name='title',
            field=models.BooleanField(default=False, verbose_name='write title name or file name to topic name'),
        ),
        migrations.AddField(
            model_name='uploaddatas',
            name='wait_time',
            field=models.PositiveIntegerField(default='0', verbose_name='input_wait_time_when_upload_file in sekund'),
        ),
    ]