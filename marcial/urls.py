from django.contrib import admin
from django.urls import path, include
from marcial import views
from django.conf.urls.static import static
from django.conf import  settings

urlpatterns = [
    path('', views.index, name='index'),
    #NAVE
    path('nave/list_nave', views.list_nave, name='list_nave'),
    path('nave/create_nave', views.create_nave, name='create_nave'),
    #path('updat_nave/', views.list_nave, name='list_nave'),

    #AERONAVE
    path('aeronave/list_aeronave/', views.list_aeronave, name='list_aeronave'),
    path('aeronave/create_aeronave', views.create_aeronave, name='create_aeronave'),

    #PASAJERO
    path('pasajero/list_pasajero/', views.list_pasajero, name='list_pasajero'),
    path('pasajero/create_pasajero', views.create_pasajero, name='create_pasajero'),

    #AEROPASAJERO
    path('aeronavepasajero/list_aeronave_pasajero/', views.list_aeronave_pasajero, name='list_aeronave_pasajero'),
    path('aeronavepasajero/create_aeronave_pasajeroin', views.create_aeronave_pasajeroIn, name='create_aeronave_pasajero'),
    path('aeronavepasajero/create_aeronave_pasajeroout', views.create_aeronave_pasajeroout, name='create_aeronave_pasajero_OUT'),

    #REVISION
    path('revision/list_revision/', views.list_revision, name='list_revision'),
    path('revision/create_revision', views.create_revision, name='create_revision'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
