# Generated by Django 4.1.2 on 2022-12-26 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadDatas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_for_get_data', models.URLField(default='https://intranet.ytit.uz/course/view.php?id=3513', max_length=300)),
                ('link_for_upload_data2', models.URLField(default='https://kiut.wisespace.uz/#/auth/login', max_length=300)),
                ('login_for_that_site2', models.CharField(max_length=300)),
                ('password_for_that_site2', models.CharField(default='password', max_length=50)),
                ('input_your_folder_path', models.CharField(default='path kiritilmagan', max_length=100)),
                ('input_level', models.CharField(choices=[('/html/body/div[1]/div[2]/div[2]/main/div[2]/div[1]/div', 'LEVEL_1'), ('/html/body/div[1]/div[2]/div[2]/main/div[2]/div[2]/div', 'LEVEL_2'), ('/html/body/div[1]/div[2]/div[2]/main/div[2]/div[3]/div', 'LEVEL_3'), ('/html/body/div[1]/div[2]/div[2]/main/div[2]/div[4]/div', 'LEVEL_4')], max_length=100)),
                ('name_of_course', models.CharField(default='course nomi kiritilmagan', max_length=70)),
                ('wait_time', models.PositiveIntegerField(default='0', verbose_name='input_wait_time_when_upload_file in sekund')),
                ('title', models.BooleanField(default=False, verbose_name='write title name to topic name')),
            ],
            options={
                'verbose_name_plural': 'upload_data',
                'db_table': 'upload_data',
            },
        ),
    ]
