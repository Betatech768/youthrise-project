# models.py
from django.db import models
from django.core.exceptions import ValidationError

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    paragraph_1 = models.TextField(blank=True, null=True)
    paragraph_2 = models.TextField(blank=True, null=True)    
    paragraph_3 = models.TextField(blank=True, null=True)
    paragraph_4 = models.TextField(blank=True, null=True) 
    Keynote = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blog_images/')

    def save(self, *args, **kwargs):
        if self.blog.images.count() >= 2:
            raise ValidationError("Maximum of 2 images allowed per blog post.")
        super().save(*args, **kwargs)
