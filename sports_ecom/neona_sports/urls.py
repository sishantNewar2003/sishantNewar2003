from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    
    path('', views.hi, name="home"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('logoutpage/', views.logoutpage, name="logoutpage"),
    path('product/', views.product, name="product"),
    path('product/<str:id>', views.product_detail, name="product_detail"),
    path('base/', views.base, name="base"),
    path('contact/', views.Contact, name="contact"),
    path('profile/', views.profile, name="profile"), 
    path('aboutus/', views.Aboutus, name='aboutus'),
 
]


