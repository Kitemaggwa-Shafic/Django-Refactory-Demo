from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# include models so that the views can use them like getting data from them
from  .models import Product  # we are importing the Product class from models to use it in our views

# we are going to include our fileters from filters file so that can be used by views.py file
from .filters import Product_Filter, Category_Filter

# Create your views here.
def index(request): 
    # creating the filter option vairables and values
    products = Product.objects.all().order_by('-id')
    products_filters = Product_Filter(request.GET, queryset = products)
    products = products_filters.qs
    return render(request, 'products/index.html', {'products':products, 'products_filters':products_filters})          # (request, 'resource to server')



@login_required  # decorators are functions to first consider running before  the procedding function below it execute
def about(request):
    return render(request, 'products/about.html') 


# creatigng a view for product_details
@login_required   
def product_details(request, product_id):
    product = Product.objects.get(id= product_id)
    return redirect(request, 'product/product_details.html', {'product':product})


@login_required
def issue_item(request, pk):
    pass

@login_required
def add_to_stock(request, pk):
    pass
