# Generated by Django 2.2.19 on 2021-12-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20211208_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voditeli',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
