from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('show/<word>', views.show),
    path('delete/<word>', views.delete)
]