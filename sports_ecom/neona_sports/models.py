from django.db import models

# Create your models here.
class Product(models.Model):
    Availibilty = (('In Stock','In Stock'), ("Out of Stock","Out of Stock"))

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=200, default='')
    price = models.IntegerField(default=0)
    sale = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    Availibilty = models.CharField(choices=Availibilty,null=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name