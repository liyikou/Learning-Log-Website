# Generated by Django 5.0.1 on 2024-06-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_vip',
            field=models.BooleanField(default=False),
        ),
    ]
