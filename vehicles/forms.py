from django import forms
from django import forms
from .models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'vehicle_id', 'vehicle_type', 'image_url',
            'checked'
        ]
