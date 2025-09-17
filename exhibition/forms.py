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
            'what_exhibiting',
        ]
        widgets = {
            'firstname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),
            'organization': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter organization name'
            }),
            'industry_segment': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter industry segment'
            }),
            'organization_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Briefly describe your organization'
            }),
            'primary_contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter primary contact number'
            }),
            'what_exhibiting': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'What are you exhibiting?'
            }),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["what_exhibiting"].label = (
            "What are you exhibiting?"
        )