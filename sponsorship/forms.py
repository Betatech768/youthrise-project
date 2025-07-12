from django import forms
from .models import Sponsors

class SponsorsForm(forms.ModelForm):
    class Meta:
        model = Sponsors
        fields = [
            'firstname',
            'lastname',
            'email',
            'contact',
            'package',
        ]
