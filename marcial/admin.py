from django.contrib import admin

# Register your models here.
from .models import Aeronave, Nave

admin.site.register(Aeronave)
admin.site.register(Nave)