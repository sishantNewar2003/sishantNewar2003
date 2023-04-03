from django.contrib import admin
from .models import Product, Contact_us, Profile, Main_category, Category

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category'  ]

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Contact_us)
admin.site.register(Profile)
admin.site.register(Main_category)
admin.site.register(Category)
