from django.db import models

# Create your models here.
#  Models are classes representing data and description from the UI web form to be stored in a DB


class Category(models.Model):
    # maxlength 50, some fields can be empty
    name = models.CharField(max_length=50, null=True, blank=True)
    #  this method gives human readable name for the object of class Categroy
    def __str__(self): #refer to this table as Category // other tables refer to it by its name
        return self.name
    


# Defining the Product Class model 
class Product(models.Model):
    #  Linking product model to categpry model, for product belongs to category
    #  FK is a column referencing in one table being used in another table
    #  This is used by a method ForeignKey()
    #  on_delete=models.CASCADE ==> will delete the the product details as long as the category is also deleted too
    categoryName = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    itemName = models.CharField(max_length=50, null=True, blank=True)
    totalQuantity = models.IntegerField(default=0, null=True, blank=True)
    issuedQuantity = models.IntegerField(default=0, null=True, blank=True)
    recievedQuantity = models.IntegerField(default=0, null=True, blank=True)
    unitPrice = models.IntegerField(default=0, null=True, blank=True)
    manufacturer = models.CharField(max_length=50, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self): #refer to this table as Category // other tables refer to it by its name
        return self.itemName
    