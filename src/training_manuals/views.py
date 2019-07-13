from django.shortcuts import render, get_object_or_404, redirect
from .models import Training_Manual
from django import forms
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
    }
    return render(request, "training_manuals/tm.html", context)


@login_required(login_url='/accounts/login/')
def tm_complete(request):
    return render(request, "training_manuals/complete.html")
