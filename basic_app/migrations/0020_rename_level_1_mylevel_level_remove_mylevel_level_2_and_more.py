# Generated by Django 4.1.2 on 2022-12-22 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0019_rename_level_l1_mylevel_level_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mylevel',
            old_name='level_1',
            new_name='level',
        ),
        migrations.RemoveField(
            model_name='mylevel',
            name='level_2',
        ),
        migrations.RemoveField(
            model_name='mylevel',
            name='level_3',
        ),
        migrations.RemoveField(
            model_name='mylevel',
            name='level_4',
        ),
    ]
