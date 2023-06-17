from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ConcesionarioForm
from .models import Concesionario
from django.contrib import messages


# Create your views here.

def index(request):
    #concesionario_list = Operador.objects.all()
    #print("Concesionarios =>", concesionario_list)
    return render(request, "empresast/index.html")


def detalle(request, operador_id):
    concesionario = get_object_or_404(Concesionario, pk=operador_id)
    return render(request, "empresast/detalle.html", {
        "concesionario": concesionario
    })


def vehiculos(request):
    # carga la pagina de vehiculos
    return render(request, "empresast/vehiculos/vehiculos.html")

#def crear_vehiculo(request):
    


def crear_operador(request):
    formulario = ConcesionarioForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Registro guardado correctamente!')
        response = redirect('empresast:concesionarios')
        return response
    return render(request, "empresast/concesionario/crear_operador.html", {'formulario': formulario})


def borrar_concesionario(request, id):
    concesionario = Concesionario.objects.get(id = id)
    concesionario.delete()
    messages.success(request, 'Registro Eliminado correctamente')
    response = redirect('empresast:concesionarios')
    return response


def editar_concesionario(request, id):
    concesionario = Concesionario.objects.get(id=id)
    formulario = ConcesionarioForm(request.POST or None, instance=concesionario)
    if formulario.is_valid and request.POST:
        formulario.save()
        messages.success(request, "Registro actualizado Correctamente")
        response = redirect('empresast:concesionarios')
        return response
    return render(request, "empresast/concesionario/editar_operador.html", {'formulario': formulario})


def vehiculos_operador(request, operador_id):
    return render(request, "empresast/vehiculos/vehiculos.html")


def concesionarios(request):
    concesionario_list = Concesionario.objects.all()
    print("Conceisonarios =>", concesionario_list)
    return render(request, "empresast/concesionario/operadores.html", 
                  {'concesionarios': concesionario_list})
