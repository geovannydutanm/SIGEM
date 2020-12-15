from django.db import models

# Create your models here.
# Create your models here.
#from __future__ import unicode_literals

from django.db import models

class Naves(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    note = models.CharField(max_length = 150)
