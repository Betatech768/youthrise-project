from django.db import models

class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
