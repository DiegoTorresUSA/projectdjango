from django.db import models

# Create your models here.

class Operador(models.Model):
    id = models.AutoField(primary_key=True)
    concesionario_nombre = models.CharField(max_length=50, verbose_name='Concesionario')
    concesionario_codigo = models.IntegerField(default=0)