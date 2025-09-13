from django import forms
from .models import Registration, RegistrationCategory


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
        exclude = ["createdat"] 
        widgets = {
            # Basic info
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter First Name", "required": True }),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Last Name", "required": True }),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Email Address", "required": True }),
            "contact": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter Contact Number", "required": True }),
            "organization": forms.TextInput(attrs={"class": "form-control", "placeholder": "Organization", "required": True }),
            "job_title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Job Title", "required": True }),

            # Choices
            "sector": forms.Select(attrs={"class": "form-select"}),
            "specify_sector": forms.TextInput(attrs={"class": "form-control", "placeholder": "If others, please specify"}),

            "leadership_position": forms.Select(attrs={"class": "form-select"}),
            "specify_other": forms.TextInput(attrs={"class": "form-control", "placeholder": "If others, please specify"}),

            "participation_source": forms.Select(attrs={"class": "form-select"}),
            "specify_source": forms.TextInput(attrs={"class": "form-control", "placeholder": "If others, please specify"}),

            "reason_for_attending": forms.CheckboxSelectMultiple(),
            "specify_reason": forms.TextInput(attrs={"class": "form-control", "placeholder": "If others, please specify"}),

            "participation_type": forms.RadioSelect(),

            # Address
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "state": forms.Select(attrs={"class": "form-select"}),

            # Relationships
            "registration_category": forms.Select(attrs={"class": "form-select"}),
            "volunteer_option": forms.Select(attrs={"class": "form-select"}),
            "specify_volunteer": forms.TextInput(attrs={"class": "form-control", "placeholder": "If others, please specify"}),
            "accessibility_accommodations": forms.CheckboxSelectMultiple(),
            "specify_accessiblity": forms.TextInput(attrs={"class": "form-control", "placeholder": "If others, please specify"}),

            # Demographics
            "age_range": forms.Select(attrs={"class": "form-select"}),
            "gender": forms.Select(attrs={"class": "form-select"}),

            # Extra info
            "covered_in_the_conference": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "additional_comments": forms.Textarea(attrs={"class": "form-control", "rows": 2}),

            # Consent
            "photography_consent": forms.Select(attrs={"class": "form-select"}),
            "email_communication": forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # List of all CharFields with choices
        choice_fields = [
            "sector",
            "leadership_position",
            "participation_source",
            "participation_type",
            "state",
            "age_range",
            "gender",
            "photography_consent",
            "email_communication",
            "registration_category",
            "volunteer_option",
        ]

        for field_name in choice_fields:
            field = self.fields.get(field_name)
            if field and field.choices:
                # Remove the blank ("---------") option if it exists
                field.choices = [c for c in field.choices if c[0] != ""]
            
        self.fields["email_communication"].label = (
            "I agree to receive conference updates and future event notifications."
        )
        self.fields["photography_consent"].label = (
            "I consent to being photographed/recorded during the conference for promotional purposes."
        )
        self.fields["additional_comments"].label = (
            "Additional Comments or Questions "
        )
        self.fields["covered_in_the_conference"].label = (
            "Is there anything specific you'd like to see covered in the conference? "
        )
        self.fields["accessibility_accommodations"].label = (
            "Do you require any accessibility accommodations? "
        )
        self.fields["volunteer_option"].label = (
            "How would you like to volunteer?"
        )
        self.fields["specify_volunteer"].label = (
            "Specify Others"
        )
        self.fields["organization"].label = (
            "Organization/Institution"
        )
        self.fields["job_title"].label = (
            "Job Title/Position"
        )
        self.fields["sector"].label = (
            "What sector do you work in?"
        )
        self.fields["leadership_position"].label = (
            "Are you in a leadership position? "
        )
        self.fields["participation_source"].label = (
            "How did you hear about this conference? "
        )
        self.fields["address"].label = (
            "Your Address"
        )
        self.fields["registration_category"].label = (
            "Are you interested in participating as? "

        )
        self.fields["participation_type"].label = (
            "How will you be attending?"

        )
        self.fields["reason_for_attending"].label = (
            "What is your primary reason for attending? (check all that applies)"

        )
        self.fields["contact"].label = (
            "Phone Number"

        )
        
        
        
        
        
        
        
class RegistrationCategoryForm(forms.ModelForm):
    class Meta:
        model = RegistrationCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name'
            })
        }
