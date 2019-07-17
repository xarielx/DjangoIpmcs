# Generated by Django 2.2.2 on 2019-07-17 01:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicles', '0002_auto_20190701_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='allowed_user',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]