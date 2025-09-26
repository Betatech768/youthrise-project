from .models import Newsletter
from django import forms


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        }
        
        error_messages = {
            "email": {
                "required": "Please provide your email address.",
                "invalid": "That doesn’t look like a valid email.",
                "unique": "This email is already subscribed.",
            }
        }