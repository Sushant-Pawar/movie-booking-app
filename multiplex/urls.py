from django.contrib import admin
from django.urls import path
from multiplex import views

urlpatterns = [
    path('', views.multiplexHome, name = "Home"),
    
]