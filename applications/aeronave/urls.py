from django.contrib import admin
from django.urls import path, include
from applications.aeronave import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.aeronaveList, name='lista_aeronaves'),
    path('aeronave/create', views.aeronave_create, name='aeronave_nueva'),
    path('aeronave/destroy', views.aeronave_delete, name='aeronave_borrar'),
    path('aeronave/update', views.aeronave_update, name='aeronave_update'),
]
