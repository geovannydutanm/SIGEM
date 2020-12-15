from django.contrib import admin
from django.urls import path
from applications.nave import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('naves/', views.naveList, name='lista_nave'),
    path('nave/create', views.nave_create, name='nave_nueva'),
    path('nave/destroy', views.aeronave_delete, name='nave_borrar'),
    path('nave/update', views.nave_update, name='nave_update'),
]