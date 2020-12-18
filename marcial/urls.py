from django.contrib import admin
from django.urls import path, include
from marcial import views
from django.conf.urls.static import static
from django.conf import  settings

urlpatterns = [
    path('', views.index, name='index'),
    #NAVE
    path('list_nave/', views.list_nave, name='list_nave'),
    path('create_nave/', views.create_nave, name='create_nave'),
    #path('updat_nave/', views.list_nave, name='list_nave'),

    #AERONAVE
    path('list_aeronave/', views.list_aeronave, name='list_aeronave'),
    path('create_aeronave/', views.create_aeronave, name='create_aeronave'),

    #PASAJERO
    path('list_pasajero/', views.list_pasajero, name='list_pasajero'),
    path('create_pasajero/', views.create_pasajero, name='create_pasajero'),

    #AEROPASAJERO
    path('list_aeronave_pasajero/', views.list_aeronave_pasajero, name='list_aeronave_pasajero'),
    path('create_aeronave_pasajero/', views.create_aeronave_pasajero, name='create_aeronave_pasajero'),

    #REVISION
    path('list_revision/', views.list_revision, name='list_revision'),
    path('create_revision/', views.create_revision, name='create_revision'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
