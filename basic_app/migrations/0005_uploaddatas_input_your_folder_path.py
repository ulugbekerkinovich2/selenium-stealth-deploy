# Generated by Django 4.1.2 on 2022-12-19 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_alter_uploaddatas_link_for_get_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploaddatas',
            name='input_your_folder_path',
            field=models.CharField(default='path kiritilmagan', max_length=40),
        ),
    ]
