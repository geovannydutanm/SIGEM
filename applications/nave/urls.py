from django.contrib import admin
from django.urls import path
from applications.nave.views import nave

urlpatterns = [
    path(r'^$', nave),
]