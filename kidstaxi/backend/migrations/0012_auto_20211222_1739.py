# Generated by Django 2.2.19 on 2021-12-22 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20211221_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='Name_man',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='voditeli',
            old_name='Name_vod',
            new_name='Name',
        ),
    ]
