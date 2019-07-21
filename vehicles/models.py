from django.db import models
import os
from django.contrib.auth.models import User
from training_manuals.models import Training_Manual as TM
from django.contrib.auth import get_user_model
# Create your models here.


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=255)
    vehicle_id = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to="img/", blank=True, null=True)
    checked = models.BooleanField(default=False)
    nfmc_step = models.ManyToManyField(TM, related_name='step')
