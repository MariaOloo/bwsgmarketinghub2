"""
URL configuration for bwsgmarketinghub2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from bwsgmarketinghub2 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Home'),
    path('about/', views.about, name='About'),
    path('products/', views.products, name='Our Services'),
    path('store/', views.store, name='Lets Work' ),
    path('discoverycall/', views.discoverycall, name='Discovery Call'),
    path('contacts/', views.contacts, name='Contacts'),
    path('quote_requests/', views.quote_requests_list, name='quote_requests_list'),
]
