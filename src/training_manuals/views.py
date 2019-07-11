from django.shortcuts import render, get_object_or_404, redirect
from .models import Training_Manual
import datetime
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def training_manual_view(request):
    obj = Training_Manual.objects.all()
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    context = {
        "tms": obj,
        "ct": current_time        
    }
    tms = Training_Manual.objects.all()
    return render(request, "training_manuals/tm_list.html", context)


@login_required(login_url='/accounts/login/')
def tm_detail_view(request, id):
    obj = get_object_or_404(Training_Manual, id=id)
    obj1 = Training_Manual.objects.get(pk=id+1)
    queryset = Training_Manual.objects.all()
    context = {
        "object": obj,
        "object_list": obj1 
    }
    return render(request, "training_manuals/tm.html", context)

    