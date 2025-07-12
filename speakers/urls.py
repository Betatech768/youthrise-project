from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_speaker, name='create_speaker'),
    path('', views.speaker_list, name='speaker_list'),
    path('speakers/edit/<int:speaker_id>/', views.edit_speaker, name='edit_speaker'),
    path('speakers/delete/<int:speaker_id>/', views.delete_speaker, name='delete_speaker'),
    
    
]
