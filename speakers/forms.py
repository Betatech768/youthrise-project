from django import forms
from .models import Speakers, SpeakerImage

class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speakers
        fields = ['Speaker_name', 'Speaker_position', 'Brief_description']

class SpeakerImageForm(forms.ModelForm):
    image = forms.ImageField(label='Upload Speaker Image')

    class Meta:
        model = SpeakerImage
        fields = ['image']
