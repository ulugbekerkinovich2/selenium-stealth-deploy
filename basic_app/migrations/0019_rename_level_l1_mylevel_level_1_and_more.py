# Generated by Django 4.1.2 on 2022-12-22 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0018_alter_mylevel_options_alter_mylevel_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mylevel',
            old_name='level_l1',
            new_name='level_1',
        ),
        migrations.RenameField(
            model_name='mylevel',
            old_name='level_l2',
            new_name='level_2',
        ),
        migrations.RenameField(
            model_name='mylevel',
            old_name='level_l3',
            new_name='level_3',
        ),
        migrations.RenameField(
            model_name='mylevel',
            old_name='level_l4',
            new_name='level_4',
        ),
    ]