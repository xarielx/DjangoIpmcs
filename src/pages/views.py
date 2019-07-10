from django.http import HttpResponse
from django.shortcuts import render
from vehicles.models import Vehicle
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

#request.user()
@login_required(login_url='/accounts/login/')
def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123
    }
    return render(request, "contact.html", my_context)