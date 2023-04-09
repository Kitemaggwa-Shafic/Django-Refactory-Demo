from django.urls import path
from dawa import views

# we are borrowing / importing from contribute package a view function resposible for managing logging
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name = 'about'), 
   
    # directing django when one open domain
    # using the contrib auth open a view link us to the login template first 
    path('', auth_views.LoginView.as_view(template_name='products/login.html'), name = 'login'),  
    path('logout/', auth_views.LogoutView.as_view(template_name='products/logout.html'), name = 'logout'), 
   
    # Url route to buy items
    # on home we look at a url of the product_detail but focusing on the product_id of the product
    path('home/<int:product_id>', views.product_details, name='product_details'), 
    path('issue_item/<str:pk>', views.issue_item, name='issue_item'), 
    path('add_to_stock/<str:pk>', views.add_to_stock, name='add_to_stock'), 
    # path('receipt/', views.receipt, name='receipt'), 
]