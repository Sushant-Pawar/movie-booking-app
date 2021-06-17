from django.contrib import admin
from django.urls import path
from authserv import views

urlpatterns = [
    path('', views.authHome),
    
]