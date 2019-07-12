from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def home_view(request, *args, **kwargs):
    if request.user.is_superuser:
        return render(request, "home.html", {})
    else:
        return redirect("/vehicles/")

# request.user()
@login_required(login_url='/accounts/login/')
def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123
    }
    return render(request, "contact.html", my_context)
    # {% if request.user.is_superuser %}
