from django import forms
from .models import Registration, RegistrationCategory


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            'first_name',
            'last_name',
            'email',
            'contact',
            'address',
            'registration_category',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),
            'contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact number'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter full address'
            }),
            'registration_category': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


class RegistrationCategoryForm(forms.ModelForm):
    class Meta:
        model = RegistrationCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name'
            })
        }
