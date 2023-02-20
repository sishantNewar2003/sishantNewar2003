from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.hi, name="home"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('logoutpage/', views.logoutpage, name="logoutpage"),
    path('product/', views.product, name="product"),
    path('cart/', views.cart, name="cart"),
    path('product/<str:id>', views.product_detail, name="product_detail"),
  
]
