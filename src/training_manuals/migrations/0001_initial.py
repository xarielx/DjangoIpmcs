# Generated by Django 2.0.7 on 2019-07-03 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training_Manual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval', models.CharField(max_length=255)),
                ('location_item_to_check', models.CharField(max_length=255)),
                ('crewmember_procedure', models.CharField(max_length=2083)),
                ('nfmc_if', models.CharField(max_length=2083)),
            ],
        ),
    ]