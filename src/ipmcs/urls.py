"""ipmcs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, contact_view
from training_manuals.views import training_manual_view, tm_detail_view
from vehicles.views import vehicle_view, vehicle_create_view
from django.views.generic.base import TemplateView

#request.user
urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('vehicles/', vehicle_view, name='vehicle'),
    path('vehicles/create/', vehicle_create_view, name='create'),
    path('training_manual/<int:id>/', tm_detail_view, name='tm-detail'),
    #path('training_manual/<int:id>', training_manual_view, name = 'tm'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
    
]
