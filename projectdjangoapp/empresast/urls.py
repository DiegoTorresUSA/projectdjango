from django.urls import path

from . import views

app_name = "empresast"

urlpatterns = [
    path("", views.index, name="index"),
    path("concesionarios", views.concesionarios, name="concesionarios"),
    path("operadores/crear", views.crear_operador, name="crear"),
    path("operadores/editar", views.editar_concesionario, name="editar"),
    path("eliminar/<int:id>", views.borrar_concesionario, name="eliminar"),
    path("operadores/editar/<int:id>", views.editar_concesionario, name="edit"),
    path("<int:operador_id>/detalle", views.detalle, name="detail"),
    path("vehiculos", views.vehiculos, name="vehiculos"),
    #path("<int:operador_id>/vehiculos", views.vehiculos_operador, name="vehiculos_operador"),

    ]
