from django.contrib import admin
from django.urls import path, include
from petswebsite import views

urlpatterns = [
    path('', views.index, name='home'),
    path('lostandFound', views.lostandFound, name='lostandFound'),
    path('adoption', views.adoption, name='adoption'),
    path('contact', views.contact, name='contact'),
]