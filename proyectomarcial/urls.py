"""proyectomarcial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
#from marcial import views

from django.conf import settings
from django.contrib.staticfiles import views
from django.urls import re_path
from marcial.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    #re_path('', include('marcial.urls')),
    re_path(r'^aeronave/', include('marcial.urls')),
    re_path(r'^nave/', include('marcial.urls')),
    re_path(r'^pasajero/', include('marcial.urls')),
    re_path(r'^aeronavepasajero/', include('marcial.urls')),
    re_path(r'^revision/', include('marcial.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]
