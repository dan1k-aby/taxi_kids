# Generated by Django 2.2.19 on 2021-12-24 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_auto_20211224_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Name_people',
        ),
        migrations.AddField(
            model_name='order',
            name='Name_people',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='backend.People'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='Name_vodil',
        ),
        migrations.AddField(
            model_name='order',
            name='Name_vodil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='backend.Voditeli'),
        ),
    ]
