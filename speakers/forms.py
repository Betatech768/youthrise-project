from django import forms
from .models import Speakers, SpeakerImage

class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speakers
        fields = ['Speaker_name', 'Speaker_position', 'Brief_description','Speaking_topic', 'Speakin_Day', 'Speaking_time']
        widgets = {
            'Speaker_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Speaker_position': forms.TextInput(attrs={'class': 'form-control'}),
            'Brief_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'Speakin_Day': forms.TextInput(attrs={'class': 'form-control'}),
            'Speaking_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'Speaking_topic': forms.TextInput(attrs={'class': 'form-control'}), 
        }
        


class SpeakerImageForm(forms.ModelForm):
    image = forms.ImageField(label='Upload Speaker Image')

    class Meta:
        model = SpeakerImage
        fields = ['image']

