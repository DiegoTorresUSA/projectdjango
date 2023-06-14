from django.db import models

# Create your models here.

class Concesionario(models.Model):
    id = models.AutoField(primary_key=True)
    concesionario_siglas = models.CharField(max_length=25, verbose_name='Siglas_Concesionario')
    concesionario_nombre = models.CharField(max_length=100, verbose_name='Concesionario')
    
    def __str__(self) -> str:
        registro = 'Siglas: ' + self.concesionario_siglas + ' - ' + 'Concesionario: ' + self.concesionario_nombre
        return registro
    
    def delete(self, using=None, keep_parents=False):
        print("Eliminado")
        super(Concesionario, self).delete()


