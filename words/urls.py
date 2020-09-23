from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('show/<word>', views.show),
    path('add', views.add_edit),
    path('edit/<word>', views.add_edit),
    path('delete/<word>', views.delete)
    
]