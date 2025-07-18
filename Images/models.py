from django.db import models

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Image {self.id}"
