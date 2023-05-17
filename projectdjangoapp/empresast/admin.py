from django.contrib import admin
from .models import Operador, Vehiculo

# Register your models here.
admin.site.register([Operador, Vehiculo])