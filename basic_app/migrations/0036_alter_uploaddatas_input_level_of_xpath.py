# Generated by Django 4.1.2 on 2022-12-26 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0035_delete_mylevel_delete_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaddatas',
            name='input_level_of_XPATH',
            field=models.CharField(choices=[('/html/body/div[1]/div[2]/div[2]/main/div[2]/div[1]/div', 'LEVEL_1'), ('2', 'LEVEL_2'), ('3', 'LEVEL_3'), ('4', 'LEVEL_4')], max_length=100),
        ),
    ]