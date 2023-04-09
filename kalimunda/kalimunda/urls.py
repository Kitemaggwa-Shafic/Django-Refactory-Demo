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
from django.urls import path, include
from django.contrib.auth import views as auth_views

# from dawa.views import index     # ==> if you use this import type, the partterns paths be like number 25
from dawa import views             # ==> if you use this import type, the partterns paths be like number 26 or 27


urlpatterns = [
    path('admin/', admin.site.urls),  
    # path('shafic/', admin.site.urls),  # adding in another user minus admin default user under admin, site urls

    # if the url in browser isnt admin / shafic , go an application dawa and look for a file urls and load them too
    path('', include('dawa.urls')),
]
