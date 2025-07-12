from django.urls import path
from .views import upload_gallery, gallery_success, gallery_list

urlpatterns = [
    path('upload/', upload_gallery, name='upload_gallery'),
    path('success/', gallery_success, name='gallery_success'),
     path('', gallery_list, name='gallery_list'),
]
