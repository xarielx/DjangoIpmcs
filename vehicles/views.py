from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle
from .forms import VehicleForm
from training_manuals.models import Training_Manual
import datetime
from django.utils import timezone

# Create your views here.

from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def vehicle_view(request, *args, **kwargs):
    vehicles = Vehicle.objects.all()
    simple = get_object_or_404(Vehicle, id=2)
    context = {
        "vehicles": vehicles,
        "simple": simple
    }
    return render(request, "vehicle/vehicle.html", context)


@login_required(login_url='/accounts/login/')
def vehicle_create_view(request):
    if request.user.is_superuser:
        form = VehicleForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = VehicleForm()
        context = {
            'form': form
        }
        return render(request, "vehicle/vehicle_create_view.html", context)
    else:
        return redirect("/#/")  # or your url name


@login_required(login_url='/accounts/login/')
def NFMC(request, id):
    veh = get_object_or_404(Vehicle, id=id)
    obj = get_object_or_404(Training_Manual, id=id)
    count = Training_Manual.objects.count()
   # obj1 = Training_Manual.objects.get(pk=id+1)
    current = Training_Manual.objects.get(pk=id).id
    prog_percent = round(((current - 0.3) / count) * 100)
    queryset = Training_Manual.objects.all()
    if current == count:
        obj1 = "complete"
    else:
        url = "training_manual/"
        cnt = current + 1  # Training_Manual.objects.get(pk=id+1)
        obj1 = url + str(cnt)

    context = {
        "object": obj,
        "object_list": obj1,
        "y": prog_percent,
        "veh": veh
    }
    return render(request, "vehicle/nfmc.html", context)
