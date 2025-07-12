from django.db import models

class Exhibition(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    organization = models.CharField(max_length=100)
    industry_segment = models.CharField(max_length=100)
    organization_description = models.TextField()
    primary_contact = models.CharField(max_length=15)
    what_are_you_exhibiting = models.CharField(max_length=50)

    def __str__(self):
        return self.organization
