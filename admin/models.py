from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='documents/pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
