# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    
   path('delete/<int:post_id>/', views.delete_blog_post, name='delete_post'),
   
]
