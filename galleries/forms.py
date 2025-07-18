from .models import Gallery, Image 
from django import forms

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'description']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image.content_type.startswith('image/'):
            raise forms.ValidationError("Only image files are allowed.")
        return image


