from django.db import models

# Create your models here.
class Sponsors(models.Model):
     
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=50)
    SPONSORSHIP_CHOICES = [
        ('basic', 'Basic Package'),
        ('premium', 'Premium'),
        ('other', 'Other'),
    ]
    package = models.CharField(
        max_length=50,
        choices=SPONSORSHIP_CHOICES,
        default='other',
    )
    
    def __str__(self):
        return self.package
