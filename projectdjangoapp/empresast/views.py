from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Operador


# Create your views here.

def index(request):
    #concesionario_list = Operador.objects.all()
    #print("Concesionarios =>", concesionario_list)
    return render(request, "empresast/index.html")


def detalle(request, operador_id):
    concesionario = get_object_or_404(Operador, pk=operador_id)
    return render(request, "empresast/detalle.html", {
        "concesionario": concesionario
    })


def vehiculos(request):
    # carga la pagina de vehiculos
    return HttpResponse(f"estas en la página de vehículos")


def crear_operador(request):
    return render(request, "empresast/concesionario/crear_operador.html")

def editar_operador(request):
    return render(request, "empresast/concesionario/editar_operador.html")


def vehiculos_operador(request, operador_id):
    return render(request, "empresast/vehiculos/vehiculos.html")


def operadores(request):
    #concesionario_list = Operador.objects.all()
    return render(request, "empresast/concesionario/operadores.html")
