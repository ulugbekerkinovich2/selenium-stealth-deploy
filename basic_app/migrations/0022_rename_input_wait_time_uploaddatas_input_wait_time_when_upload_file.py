# Generated by Django 4.1.2 on 2022-12-24 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0021_uploaddatas_input_wait_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploaddatas',
            old_name='input_wait_time',
            new_name='input_wait_time_when_upload_file',
        ),
    ]