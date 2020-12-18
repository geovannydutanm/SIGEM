from django.contrib import admin

# Register your models here.
from .models import Aeronave, Nave, Pasajero, Aeronave_Pasajero, Revision

admin.site.register(Aeronave)
admin.site.register(Nave)
admin.site.register(Pasajero)
admin.site.register(Aeronave_Pasajero)
admin.site.register(Revision)