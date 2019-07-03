from django.shortcuts import render
from .models import Vehicle
from .forms import VehicleForm
# Create your views here.

def vehicle_view(request, *args, **kwargs):
    vehicles = Vehicle.objects.all()
    return render(request, "vehicle/vehicle.html", {'vehicles': vehicles})

def vehicle_create_view(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form': form
    }
    return render(request, "vehicle/vehicle_create_view.html", context)

