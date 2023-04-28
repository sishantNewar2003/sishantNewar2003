"""sports_ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from neona_sports import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('neona_sports.urls')),
    path('signup/', views.signup, name="signup"),

    # Add to cart functinality
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    path("accounts/", include("django.contrib.auth.urls")),

    # Reset password
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    # admin contacts
    path('adminpanel/', views.admin, name="adminpanel"),
    path('add/',views.ADD, name='add'),
    path('edit', views.Edit, name='edit'),
    path('update/<str:id>', views.Update, name='update'),
    path('delete/<str:id>', views.Delete, name="delete"),

    
    path('changepass/', views.Changepass, name="changepass"),
    
    #admin login
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('dashboard/', views.dashboard, name="dashboard"),

    # admin Products
    path('prodadmin/', views.prodadmin, name="prodadmin"),
    path('add-product/', views.addProduct, name="add-product"),
    path('edit-product/<str:st>', views.editProduct, name="edit-product"),
    path('delete-product/<str:st>', views.deleteProduct, name="delete-product"),

    #wishlist
    path('wishlist/',views.Wishlist, name='wishlist'),

    #khalti
    path('khalti', views.khalti, name='khalti'),
    path('khalti-verify/', views.khalti_verify, name='khaltiverify'),

    #Checkout
    path('checkout', views.Checkout, name='checkout'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
