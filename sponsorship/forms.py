from django import forms
from .models import Sponsors,SponsorshipPackage


class SponsorshipPackageForm(forms.ModelForm):
    class Meta:
        model = SponsorshipPackage
        fields = ['name', 'price']  # Fields from the model
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter package name'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price',
                'step': '0.01'  # allows decimal input
            }),
        }

class SponsorsForm(forms.ModelForm):
    class Meta:
        model = Sponsors
        fields = ['firstname', 'lastname', 'email', 'contact', 'package']
        widgets = {
            'firstname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your first name'
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),
            'package': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id_package'  # important for JS hook
            }),
        }