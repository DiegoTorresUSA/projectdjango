from django.urls import path

from . import views

app_name = "empresast"

urlpatterns = [
    path("", views.index, name="index"),
    path("operadores", views.operadores, name="operadores"),
    path("operadores/crear", views.crear_operador, name="crear"),
    path("<int:operador_id>/detalle", views.detalle, name="detail"),
    path("vehiculos", views.vehiculos, name="vehiculos"),
    path("<int:operador_id>/vehiculos", views.vehiculos_operador, name="vehiculos_operador"),

    ]
