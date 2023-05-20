from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Operador, Vehiculo

# Create your views here.

def index(request):
    concesionario_list = Operador.objects.all()
    return render(request, "empresast/index.html",{
        "concesionario_list": concesionario_list
    })



def detalle(request, operador_id):
    concesionario = get_object_or_404(Operador, pk=operador_id)    
    return render(request, "empresast/detalle.html", {
        "concesionario": concesionario
    })
    


def vehiculos(request, operador_id):
    return HttpResponse(f"estas en la relación de vehículos de cada concesionario {operador_id}")


def operadores(request):
    concesionario_list = Operador.objects.all()
    return render(request, "empresast/operadores.html",{
        "concesionario_list": concesionario_list
    })