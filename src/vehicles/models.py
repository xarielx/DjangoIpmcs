from django.db import models
import os
from django.contrib.auth.models import User
from training_manuals.models import Training_Manual as TM
from django.contrib.auth import get_user_model


def get_image_path(instance, filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(BASE_DIR, 'static')

# Create your models here.
class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=255)
    vehicle_id = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to=get_image_path("img/", vehicle_id), blank=True, null=True)
    checked = models.BooleanField(default=False)
    nfmc_step = models.ManyToManyField(TM, related_name='step')
    updated = models.DateTimeField(auto_now=True)
