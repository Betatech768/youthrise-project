from django.contrib import admin
from .models import BlogPost, BlogImage

# Inline for uploading multiple images under one blog post
class BlogImageInline(admin.TabularInline):  # Use StackedInline for image previews
    model = BlogImage
    extra = 1  # Number of empty forms shown by default
    max_num = 2  # Limit to 2 images

# Admin for BlogPost with inline images
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [BlogImageInline]

# Register both models
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogImage)  # Optional: Only if you want to manage images separately
