"""kalimunda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
# from django.contrib.auth import views as auth_views

# from dawa.views import index     # ==> if you use this import type, the partterns paths be like number 25
from dawa import views             # ==> if you use this import type, the partterns paths be like number 26 or 27


urlpatterns = [
    path('admin/', admin.site.urls),  
    # path("index/", index, name ="index"), 
    path("index/", views.index, name ="index"), 
    path("home/", views.index, name ="home"), 
    path('about/', views.about, name = 'about'),  
    # path('', auth_views.LoginView.as_view(template_name='product/login.html'), name = 'login'),  
    # path('', auth_views.LogoutView.as_view(template_name='product/logout.html'), name = 'logout'), 
   
   
    # Url route to buy items
    # on home we look at a url of the product_detail but focusing on the product_id of the product
    # path('home/<int:product_id>', views.product_detail, name='product_detail'), 
    # path('issue_item/<str:pk>', views.issue_item, name='issue_item'), 
    # path('add_to_stock/<str:pk>', views.add_to_stock, name='add_to_stock'), 
]
