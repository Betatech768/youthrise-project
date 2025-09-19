from django.db import models


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="uploads/sponsors/")

    def __str__(self):
        return self.name


class stream(models.Model):
    streaming_url = models.URLField(max_length=200, blank=True, null=True)
    
    
    


class Work(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class stories(models.Model):
    fullname = models.CharField(max_length=255)
    organization = [
        ("NGO", "NGO"),
        ("Community groups", "Community groups"), ("Faith-Based Organization", "Faith-Based Organization"),
        ("Association or Union", "Association or Union"), 
        ("Others", "Others")
    ]
    specify_others = models.CharField(max_length=100, blank=True)
    content = models.CharField(max_length=255, choices=organization, )
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
    Location = models.CharField(max_length=20, choices=NIGERIAN_STATES)
    implementing = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    contact_person_email = models.EmailField(max_length=255)
    contact_person_phone = models.CharField(max_length=20)
    work_impact = models.ForeignKey(Work, on_delete=models.CASCADE)
    specify_others = models.CharField(max_length=100, blank=True)
    describe_story = models.TextField()
    make_difference = models.TextField()
    CONSENT_CHOICES = [
    ("Yes, I would like to speak", "Yes, I would like to speak"),
    ("No, but I am open to my story being shared", "No, but I am open to my story being shared"),
]
    speak_about = models.CharField(max_length=100, choices=CONSENT_CHOICES)
    organization_website = models.URLField(max_length=200, blank=True)
    portfolio_link = models.URLField(max_length=200)
    social_media = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Fullname
    
    
    
