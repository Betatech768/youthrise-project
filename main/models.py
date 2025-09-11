from django.db import models


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="uploads/sponsors/")

    def __str__(self):
        return self.name


class stream(models.Model):
    streaming_url = models.URLField(max_length=200, blank=True, null=True)