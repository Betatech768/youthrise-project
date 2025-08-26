from django.db import models

class RegistrationCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    registration_category = models.ForeignKey(RegistrationCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
