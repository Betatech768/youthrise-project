from django import forms
from . models import stream, stories


class StreamForm(forms.ModelForm):
    class Meta:
        model = stream
        fields = ['streaming_url']
        widgets = {
            "streaming_url": forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter Youtube Streaming URL"}),
        }   
        
        
        

class StoriesForm(forms.ModelForm):
    class Meta:
        model = stories
        fields = [
            "fullname",
            "content",
            "specify_others",
            "Location",
            "implementing",
            "contact_person",
            "contact_person_email",
            "contact_person_phone",
            "work_impact",
            "specify_works",
            "describe_story",
            "make_difference",
            "speak_about",
            "organization_website",
            "portfolio_link",
            "social_media",
        ]
        widgets = {
            "fullname": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter full name"}),
            "content": forms.Select(attrs={"class": "form-select"}),
            "Location": forms.Select(attrs={"class": "form-select"}),
            "implementing": forms.TextInput(attrs={"class": "form-control", "placeholder": "Implementing organization"}),
            "contact_person": forms.TextInput(attrs={"class": "form-control", "placeholder": "Contact person"}),
            "contact_person_email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "contact_person_phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone number"}),
            "work_impact": forms.Select(attrs={"class": "form-select"}),
            "specify_others": forms.TextInput(attrs={"class": "form-control", "placeholder": "If others, please specify"}),
            "describe_story": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Describe your story"}),
            "make_difference": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "How did it make a difference?"}),
            "speak_about": forms.Select(attrs={"class": "form-select"}),
            "organization_website": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://example.com"}),
            "portfolio_link": forms.URLInput(attrs={"class": "form-control", "placeholder": "Portfolio link"}),
            "social_media": forms.URLInput(attrs={"class": "form-control", "placeholder": "Social media link"}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # List of all CharFields with choices
        choice_fields = [
            "content",
            "speak_about",
            "work_impact",
            "Location",
            
        ]

        for field_name in choice_fields:
            field = self.fields.get(field_name)
            if field and field.choices:
                # Remove the blank ("---------") option if it exists
                field.choices = [c for c in field.choices if c[0] != ""]
            
        self.fields["content"].label = (
            "Type Of Organization/Individual"
        )
        self.fields["implementing"].label = (
            "How long have you been implementing?"
        )
        self.fields["contact_person"].label = (
            "Contact Person (Full Name)"
        )
        self.fields["contact_person_email"].label = (
            "Email Address"
        )
        self.fields["contact_person_phone"].label = (
            "Phone Number/WhatsApp"
        )
        self.fields["work_impact"].label = (
            "Which group(s) of young people does your work impact most?"
        )
        self.fields["describe_story"].label = (
            "Please briefly describe your story of impact (max 300 words)"
        )
        self.fields["make_difference"].label = (
            "How did your work make a difference? (max 200 words)"
        )
        self.fields["speak_about"].label = (
            "Would you like to speak at the We Are People Conference 2025?"
        )
        self.fields["organization_website"].label = (
            "Organization Website (if any)"
        )
        self.fields["portfolio_link"].label = (
            "Portfolio Link (if any)"
        )
        self.fields["social_media"].label = (
            "Social Media Link (if any)"
        )
        self.fields["specify_others"].label = (
            "Others (please specify)"
        )
        self.fields["specify_works"].label = (
            "Others (please specify)"
        )