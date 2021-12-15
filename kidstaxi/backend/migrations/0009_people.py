# Generated by Django 2.2.19 on 2021-12-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20211209_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15, verbose_name='Имя')),
                ('Sure_name', models.CharField(max_length=15, verbose_name='Фамилия')),
                ('Number', models.CharField(max_length=20, verbose_name='Номер телефона')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
