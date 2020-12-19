from time import timezone

from django.db import models

# Create your models here.
#MODELO NAVE
class Nave(models.Model):
    name = models.CharField(max_length = 50)



#MODELO PASAJERO
class Pasajero(models.Model):
    name = models.CharField(max_length = 100)
    credencial = models.CharField(max_length=50, null=True, default=None)
    fecha_ultimoregistro = models.DateField(auto_now=True)

#MODELO AERONAVE
class Aeronave(models.Model):
    name = models.CharField(max_length=50)
    num_max = models.IntegerField()
    nave_origen = models.ForeignKey(Nave, related_name = 'naves_origen', on_delete=models.CASCADE, null=True, default=None)
    nave_destino = models.ForeignKey(Nave, related_name='naves_destino',  on_delete=models.CASCADE, null=True, default=None)
    lista_pasajeros = models.ManyToManyField(Pasajero, related_name='listado_pasajeros')


#MODELO AERONAVE PASAJERO
class Aeronave_Pasajero(models.Model):
    fecha_registra = models.DateTimeField(auto_now=True)
    ingresa_aeronave = models.BooleanField()
    aeronave = models.ForeignKey(Aeronave, related_name='aeronaves_aeropasajero', on_delete=models.CASCADE, null=True, default=None)
    pasajero = models.ForeignKey(Pasajero, related_name='pasajeros_aeropasajero', on_delete=models.CASCADE, null=True, default=None)


#REVISION
class Revision(models.Model):
    name = models.CharField(max_length = 100)
    fecha_registra = models.DateTimeField("Fecha Registra")
    aeronave = models.ForeignKey(Aeronave, related_name='aeronaves_revision', on_delete=models.CASCADE)
    pasajeros = models.ManyToManyField(Pasajero, related_name='revisiones')

    class Meta:
        ordering = ("fecha_registra",)

'''
class DetalleRevision(models.Model):
    revision = models.ForeignKey(Revision, related_name='revision_detalle', on_delete=models.CASCADE())
    name = models.CharField(max_length = 100)
    fecha_registra = models.DateTimeField(default=timezone.now)
    pasajero = models.ForeignKey(Pasajero, related_name='pasajero_detalle', on_delete=models.CASCADE, null=True, default=None)

'''

