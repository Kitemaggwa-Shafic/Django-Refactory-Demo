from django.contrib import admin

from . models import *     #  . and + is polymophic signs and can be used to access all method of class, 

# from models import Category  # This is another way of importing class by class 

# Register your models here.

admin.site.register(Category)   # Registering category class from models.py file into the admin to add it to the admin UI
admin.site.register(Product)   # Registering the Product model in admin
