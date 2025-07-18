from django import forms
from .models import GalleryImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['image', 'title']  # include 'title' if needed

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("Please upload an image.")
        return image
