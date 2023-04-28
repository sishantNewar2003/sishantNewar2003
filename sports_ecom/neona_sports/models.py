from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from datetime import datetime, date



# Create your models here.


class Contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
    

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'    
  

class Main_category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    main_category = models.ForeignKey(Main_category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Product(models.Model):
    Availibilty = (('In Stock','In Stock'), ("Out of Stock","Out of Stock"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='1')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=200, default='')
    price = models.IntegerField(default=0)
    sale = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    Availibilty = models.CharField(choices=Availibilty,null=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
   

    def __str__(self):
        return self.name

class Customer(models.Model):
    name=models.CharField(max_length=50, null=True)
    phone=models.CharField(max_length=50, null=True)
    email=models.EmailField()
    date_created=models.DateTimeField(auto_now_add=True, null=True)

    
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS={
        ('pending', 'pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered','Delivered'),

    }
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=100,null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    amount = models.CharField(max_length=100, null=True)
    payment_completed = models.BooleanField(default=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


      
    # def __str__(self):
    #     return self.user


class order_items(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product=models.CharField(max_length=200)
    image=models.ImageField(upload_to='products/')
    quantity=models.CharField(max_length=20)
    price=models.CharField(max_length=50)
    total=models.CharField(max_length=1000)

    # def __str__(self):
    #     return self.user