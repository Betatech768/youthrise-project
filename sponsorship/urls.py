from django.urls import path
from . import views

urlpatterns = [
    path('sponsors/register/', views.sponsorship_form_view, name='sponsorship_form'),
    path('sponsors/list/', views.sponsors_list_view, name='sponsors_list'),
]
