from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='register'),
    path('registrations_list/', views.registration_list_view, name='registration_list'),
]
