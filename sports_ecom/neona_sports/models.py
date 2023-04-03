from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User



# Create your models here.


class Contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    # phone_number =  models.CharField(max_length=12)
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
   

    
    def img_preview(self): 
        return mark_safe('<img src = "{}" width = "300"/>'.format(url = self.image.url ))

    

    def __str__(self):
        return self.name
