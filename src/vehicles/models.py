from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=255)
    vehicle_id = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2083)
    checked = models.BooleanField(default=False)
    allowed_user = models.ManyToManyField(User, blank=True, null=True)