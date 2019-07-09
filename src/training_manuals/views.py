from django.shortcuts import render
from .models import Training_Manual
# Create your views here.

def training_manual_view(request, *args, **kwargs):
    tms = Training_Manual.objects.all()
    return render(request, "training_manuals/tm.html", {'tms': tms})
