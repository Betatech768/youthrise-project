from django.contrib import admin
from .models import Gallery, Image

# Register your models here.
admin.site.register(Gallery)
# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'uploaded_at')