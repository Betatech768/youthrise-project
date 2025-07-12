# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_and_list_blog_posts, name='create_post'),
    path('edit/<int:post_id>/', views.edit_blog_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_blog_post, name='delete_post'),
   
]
