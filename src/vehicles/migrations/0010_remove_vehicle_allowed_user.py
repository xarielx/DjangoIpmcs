# Generated by Django 2.2.2 on 2019-07-18 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0009_vehicle_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='allowed_user',
        ),
    ]
