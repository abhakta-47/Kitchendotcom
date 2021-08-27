"""Kitchendotcom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from home import views
urlpatterns = [
    path("", views.kitchen_price_steps, name='home'),
    path("select_layout", views.select_layout, name='select_layout'),
    path("customer_details", views.customer_details, name='customer_details'),
    path("select_lshape", views.lshape, name='select_lshape'), 
    path("select_ushape", views.ushape, name='select_ushape'), 
    path("select_straight", views.straight, name='select_straight'), 
    path("select_parallel", views.parallel, name='select_parallel'),
    path("select_countertop", views.select_countertop, name='select_countertop'), 
    path("select_loft", views.select_loft_type, name='select_loft') 
]