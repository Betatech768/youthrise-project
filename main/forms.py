from django import forms
from . models import stream


class StreamForm(forms.ModelForm):
    class Meta:
        model = stream
        fields = ['streaming_url']
        widgets = {
            "streaming_url": forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter Youtube Streaming URL"}),
        }   