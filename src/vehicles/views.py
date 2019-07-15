from django.shortcuts import render, redirect
from .models import Vehicle
from .forms import VehicleForm
# Create your views here.

from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def vehicle_view(request, *args, **kwargs):
    vehicles = Vehicle.objects.all()
    return render(request, "vehicle/vehicle.html", {'vehicles': vehicles})


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
