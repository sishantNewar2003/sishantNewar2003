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
    path('wishlist/', views.wishlist, name='wishlist'),
    path('adminpanel/', views.admin, name="admin"),
    path('add/',views.ADD, name='add'),
    path('edit', views.Edit, name='edit'),
    path('update/<str:id>', views.Update, name='update'),
    path('delete/<str:id>', views.Delete, name="delete"),
    path('changepass/', views.Changepass, name="changepass"),
    path('prodadmin/', views.prodadmin, name="prodadmin"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminsignup/', views.adminsignup, name="adminsignup"),
    path('dashboard/', views.dashboard, name="dashboard"),
    

    

    


  
]
