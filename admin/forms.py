from django import forms
from .models import Document, ConferenceDate, ConferenceVenue, ViewingDays
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
        
        
        
class ConferenceDateForm(forms.ModelForm):
    class Meta:
        model = ConferenceDate
        fields = ['start_date', 'end_date']
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "end_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }
        
        def clean(self):
            cleaned_data = super().clean()
            if ConferenceDate.objects.exists() and not self.instance.pk:
                raise forms.ValidationError("Only one Conference Date instance is allowed.")
            return cleaned_data

        
class ConferenceVenueForm(forms.ModelForm):
    
    class Meta:
        model = ConferenceVenue
        fields = ['venue']
        widgets = {
            "venue": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Conference Venue"}),
        }
   
        
        
class ViewingDaysForm(forms.ModelForm):
    class Meta:
        model = ViewingDays
        fields = ['category', 'video_link']
        widgets = {
            "category": forms.Select(attrs={"class": "form-control"}),
            "video_link": forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter Youtube URL"}),
        }


