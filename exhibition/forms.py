from django import forms
from  .models import Exhibition

from django import forms
from .models import Exhibition

class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = [
            'firstname',
            'lastname',
            'email',
            'organization',
            'industry_segment',
            'organization_description',
            'primary_contact',
            'what_are_you_exhibiting'
        ]
