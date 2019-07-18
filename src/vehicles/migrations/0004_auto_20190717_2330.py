# Generated by Django 2.2.2 on 2019-07-18 03:30

from django.db import migrations, models
import vehicles.models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_vehicle_allowed_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=vehicles.models.get_image_path),
        ),
    ]