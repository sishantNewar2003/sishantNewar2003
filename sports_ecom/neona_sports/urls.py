from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.hi, name="home"),
    path('login/', views.login, name="login"),
    
]
