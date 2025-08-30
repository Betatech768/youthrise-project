from django.db import models

# Create your models here.


class SponsorshipPackage(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ₦{self.price:,.2f}"


class Sponsors(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=50)

    package = models.ForeignKey(SponsorshipPackage, on_delete=models.CASCADE)

    def __str__(self):
      return f"{self.firstname} {self.lastname} → {self.package}"
