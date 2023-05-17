from django.shortcuts import render
from django.http import HttpResponse

from .models import Operador, Vehiculo

# Create your views here.

def index(request):
    concesionario_list = Operador.objects.all()
    return render(request, "empresast/index.html", {
        "concesionario_list": concesionario_list
    })


def detalle(request, operador_id):
    return HttpResponse(f"estas en el detalle del concesionario {operador_id}")


def vehiculos(request, operador_id):
    return HttpResponse(f"estas en la relación de vehículos de cada concesionario {operador_id}")