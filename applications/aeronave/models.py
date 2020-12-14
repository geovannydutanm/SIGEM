from django.db import models

# Create your models here.
#from __future__ import unicode_literals

from django.db import models
class aeronave(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    num_max = models.IntegerField()

