from django.db import models

class RegistrationCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ReasonForAttending(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class AccessibilityOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Registration(models.Model):
    # Basic info
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.BigIntegerField(blank=True)
    organization = models.CharField(max_length=200, blank=True)
    job_title = models.CharField(max_length=100)

    # Sector choices
    SECTOR_CHOICES = [
        ("NGO", "Non-profit/NGO"),
        ("Government", "Government"),
        ("Private Sector", "Private Sector/Corporate"),
        ("Education/Academia", "Education/Academia"),
        ("Healthcare", "Healthcare"),
        ("Media/Comm", "Media/Communication"),
        ("Student", "Student"),
        ("Others", "Others"),
    ]
    sector = models.CharField(max_length=50, choices=SECTOR_CHOICES)
    specify_sector = models.CharField(max_length=100, blank=True)

    # Leadership
    LEADER_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No"),
        ("Others", "Others"),
        
    ]
    leadership_position = models.CharField(max_length=10,blank=True, choices=LEADER_CHOICES)
    specify_other = models.CharField(max_length=100, blank=True)

    # Participation source
    SOURCE_CHOICES = [
        ("Social Media", "Social Media"),
        ("Email Invitation", "Email Invitation"),
        ("Colleague", "Colleague"),
        ("Website", "Website"),
        ("Partner Organization", "Partner Organization"),
        ("Others", "Others"),
    ]
    participation_source = models.CharField(max_length=50, choices=SOURCE_CHOICES, blank=True)
    specify_source = models.CharField(max_length=100, blank=True)



    #  Reasons for atteding 
    
    reason_for_attending = models.ManyToManyField(ReasonForAttending, blank=True)
    specify_reason = models.CharField(max_length=100, blank=True)

    
    # Participation type
    PARTICIPATION_TYPE_CHOICES = [
        ("ip", "In-person"),
        ("virtual", "Virtual/Online"),
        ("hybrid", "Hybrid (some sessions in-person, some virtual)"),
    ]
    participation_type = models.CharField(max_length=20, blank=True, choices=PARTICIPATION_TYPE_CHOICES)

    # Address
    address = models.CharField(max_length=200, blank=True)

    # Nigerian States
    NIGERIAN_STATES = [
        ("ABIA", "Abia"),
        ("ADAMAWA", "Adamawa"),
        ("AKAW", "Akwa Ibom"),
        ("ANAMBRA", "Anambra"),
        ("BAUCHI", "Bauchi"),
        ("BAYELSA", "Bayelsa"),
        ("BENUE", "Benue"),
        ("BORNO", "Borno"),
        ("CROSS-RIVER", "Cross River"),
        ("DELTA", "Delta"),
        ("EBONYI", "Ebonyi"),
        ("EDO", "Edo"),
        ("EKITI", "Ekiti"),
        ("ENUGU", "Enugu"),
        ("FCT", "Federal Capital Territory (Abuja)"),
        ("GOMBE", "Gombe"),
        ("IMO", "Imo"),
        ("JIGAWA", "Jigawa"),
        ("KADUNA", "Kaduna"),
        ("KANO", "Kano"),
        ("KATSINA", "Katsina"),
        ("KEBBI", "Kebbi"),
        ("KOGI", "Kogi"),
        ("KWARA", "Kwara"),
        ("LAGOS", "Lagos"),
        ("NASARAWA", "Nasarawa"),
        ("NIGER", "Niger"),
        ("OGUN", "Ogun"),
        ("ONDO", "Ondo"),
        ("OSUN", "Osun"),
        ("OYO", "Oyo"),
        ("PLATEAU", "Plateau"),
        ("RIVERS", "Rivers"),
        ("SOKOTO", "Sokoto"),
        ("TARABA", "Taraba"),
        ("YOLA", "Yobe"),
        ("ZAMFARA", "Zamfara"),
    ]
    state = models.CharField(max_length=20, choices=NIGERIAN_STATES)

    # Relationships
    
    registration_category = models.ForeignKey(RegistrationCategory, on_delete=models.CASCADE)
    
    volunteering = [("Ushering", "Ushering"), ("Media coverage", "Media coverage"), ("Rapporteur", "Rapporteur"), ("Security", "Security"), ("Audio and Visual Tech", "Audio and Visual Tech"), ("Other", "Other")]
    
    volunteer_option = models.CharField(max_length= 30, choices=volunteering, null=True, blank=True)
    
    specify_volunteer = models.CharField(max_length=100, blank=True)
   
    accessibility_accommodations = models.ManyToManyField(
        AccessibilityOption,
        blank=True,
    )
    specify_accessiblity  = models.CharField(max_length=50, blank=True)
    AGE_RANGE_CHOICES = [
    ("18-25", "18–25"),
    ("26-35", "26–35"),
    ("36-45", "36–45"),
    ("46-55", "46–55+"),
]


    age_range = models.CharField(
    max_length=10,
    choices=AGE_RANGE_CHOICES,
    blank=True
)   
    GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Prefer not to say", "Prefer not to say"),
]
    gender = models.CharField(
    max_length=20,
    choices=GENDER_CHOICES,
    blank=True
)
    covered_in_the_conference = models.CharField( max_length=200, blank=True)
    additional_comments = models.CharField( max_length=100, blank= True)
    
    CONSENT_CHOICES2= [
      ("Agree", "I agree"),  
      ("Disagree", "I Disagree"),
    ]
    
    
    CONSENT_CHOICES = [
    ("Agree", "I agree"),
    ("Disagree", "I disagree"),
]
    photography_consent = models.CharField(
        max_length=10,
        choices= CONSENT_CHOICES2,
        blank=False,
    )

    # Email communication consent
    email_communication = models.CharField(
        max_length=10,
        choices=CONSENT_CHOICES,
        blank=False,
    )
    registered_on = models.DateField(auto_now_add=True)
    
    def get_fields(self):
        """Return (verbose_name, value) for all fields, including M2M, FK, and choices as string."""
        fields = []
        for field in self._meta.fields:
            value = field.value_from_object(self)

            # Handle ForeignKey
            if field.many_to_one and value is not None:
                related_obj = getattr(self, field.name)
                value = str(related_obj) if related_obj else None

            # Handle choices (convert DB value to human-readable label)
            elif field.choices:
                if not value:  # None or ""
                    value = ""
                else:
                    value = dict(field.flatchoices).get(value, value)

            fields.append((field.verbose_name, value))

        # Handle ManyToMany
        for field in self._meta.many_to_many:
            value = getattr(self, field.name).all()
            value = ", ".join(str(obj) for obj in value)
            fields.append((field.verbose_name, value))

        return fields