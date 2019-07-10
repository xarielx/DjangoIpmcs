from django.db import models
from django.urls import reverse

# Create your models here.
class Training_Manual(models.Model):
    interval = models.CharField(max_length=255)
    location_item_to_check = models.CharField(max_length=255)
    crewmember_procedure = models.CharField(max_length=2083)
    nfmc_if = models.CharField(max_length=2083)


def get_absolute_url(self):
    return reverse("tm-detail", kwargs={"id": self.id})
