from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Operador, Vehiculo

# Create your views here.

def index(request):
    concesionario_list = Operador.objects.all()
    print(concesionario_list)
    return render(request, "empresast/index.html",{
        "concesionario_list": concesionario_list
    })


def detalle(request, operador_id):
    return HttpResponse(f"estas en la relación de vehículos de cada concesionario {operador_id}")


def vehiculos(request, operador_id):
    return HttpResponse(f"estas en la relación de vehículos de cada concesionario {operador_id}")