from django.db import models



class Speakers(models.Model):
    Speaker_name = models.CharField (max_length=50)
    Speaker_position = models.CharField(max_length=100)
    Speaking_topic = models.CharField(max_length=200, default="To be announced", blank=True)
    Speakin_Day = models.CharField(max_length=100, null= True)
    Speaking_time = models.TimeField(null= True)
    Brief_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Speaker_name

class SpeakerImage(models.Model):
    blog = models.ForeignKey(Speakers, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='speaker_images/')
    
    
    
    