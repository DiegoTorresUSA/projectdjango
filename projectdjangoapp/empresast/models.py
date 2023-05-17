from django.db import models

# Create your models here.

class Operador(models.Model):
    concesionario_nombre = models.CharField(max_length=50)
    concesionario_codigo = models.IntegerField(default=0)
  
    def __str__(self):    
        concesionario_nombre = self.concesionario_nombre
        return concesionario_nombre
    
class Vehiculo(models.Model):
    concesionario = models.ForeignKey(Operador, on_delete=models.CASCADE)
    placa = models.CharField(max_length=7)
    fecha_vinculacion = models.DateField("Fecha vinculación")
    modelo = models.IntegerField(default=0)
    tipologia = models.CharField(max_length=20)

    def __str__(self):
        placa = self.placa
        return placa
    



  
