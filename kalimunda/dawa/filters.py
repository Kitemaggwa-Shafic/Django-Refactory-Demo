# this module django_filters is used to serach for data from other data
import django_filters

from .models import Category, Product



# creating a class to filter objects from our models imported
class Product_Filter(django_filters.FilterSet): #from django_filter module we need only filterSet function
    class Meta: # tempolary class used to alter the content of another class
        model = Product
        fields = ['itemName'] # we need only the user to serach for itemName only but you can add other fields to
        # fields = ['itemName', 'totalQuantity', 'unitPrice', 'manufacturer', 'brand']


class Category_Filter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['name']