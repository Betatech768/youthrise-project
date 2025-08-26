from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('faqs/', views.faqs, name='faqs'),
    path('blog/', views.bloglist, name='blog'),
    path('bloglist/<int:blog_id>', views.blog, name='bloglist'),
    path('sponsors/', views.sponsor, name= 'sponsor'),
    path('exhibitions/', views.exhibition, name= 'exhibitions'),
    path('contact-us/', views.contact, name= 'contact'),
    path('registration/', views.registration, name= 'registration'),
    path('speakers/', views.speakers, name= 'speakers'),
    path('sponsors/', views.sponsorship_form_view, name='sponsorship_form'),
    path('gallery/', views.gallery_list, name='gallery_list_main'),
    path('speaker/<int:speaker_id>/', views.speaker_details, name='speaker_details'),
]
