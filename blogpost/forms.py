# forms.py
from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'paragraph_1', 'paragraph_2', 'paragraph_3', 'paragraph_4', 'Keynote']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'paragraph_1': forms.Textarea(attrs={'class': 'form-control'}),
            'paragraph_2': forms.Textarea(attrs={'class': 'form-control'}),
            'paragraph_3': forms.Textarea(attrs={'class': 'form-control'}),
            'paragraph_4': forms.Textarea(attrs={'class': 'form-control'}),
            'Keynote': forms.Textarea(attrs={'class': 'form-control'}),
        }
