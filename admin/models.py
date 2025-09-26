from django.db import models
from django.core.exceptions import ValidationError 

class Document(models.Model):
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='documents/pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ConferenceDate(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if ConferenceDate.objects.exists() and not self.pk:
            raise ValidationError("Only one Conference Date instance is allowed.")

    @property
    def day_month_ordinal(self):
        day = self.date.day
        # Determine ordinal suffix
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "TH"
        else:
            suffix = ["ST", "ND", "RD"][day % 10 - 1]
        month = self.date.strftime("%B")
        return f"{day}{suffix} {month}"
    def __str__(self):
        return "Conference Date"
    
    
    
class ConferenceVenue(models.Model):
    venue = models.CharField(max_length=200)

    def clean(self):
        if ConferenceVenue.objects.exists() and not self.pk:
            raise ValidationError("Only one Conference Venue instance is allowed.")


    def __str__(self):
        return "Conference Venue"
    

class ViewingDaysCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    
class ViewingDays(models.Model):
    category = models.ForeignKey(ViewingDaysCategory, on_delete=models.CASCADE, related_name='viewing')
    video_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.category.name    