# yourapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.exhibition_view, name='exhibition'),
    path('list/', views.exhibition_list_view, name='exhibition_list'),
]
