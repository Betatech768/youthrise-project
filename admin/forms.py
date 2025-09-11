from django import forms
from .models import Document
from main.models import Sponsor
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))




class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'pdf']


class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['name', 'logo']