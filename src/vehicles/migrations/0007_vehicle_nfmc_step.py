# Generated by Django 2.2.2 on 2019-07-18 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_manuals', '0001_initial'),
        ('vehicles', '0006_auto_20190718_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='nfmc_step',
            field=models.ManyToManyField(default=0, to='training_manuals.Training_Manual'),
        ),
    ]
