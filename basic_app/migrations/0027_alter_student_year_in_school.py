# Generated by Django 4.1.2 on 2022-12-25 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0026_student_alter_uploaddatas_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year_in_school',
            field=models.CharField(choices=[('/html/body/div[1]/div[2]/div[2]/main/div[2]/div[1]/div', 'LEVEL_1'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='/html/body/div[1]/div[2]/div[2]/main/div[2]/div[1]/div', max_length=100),
        ),
    ]