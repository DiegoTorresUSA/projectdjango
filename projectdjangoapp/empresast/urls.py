from django.urls import path

from . import views

app_name = "empresast"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:operador_id>/detalle", views.detalle, name="detail"),
    path("<int:operador_id>/vehiculos", views.vehiculos, name="vehiculos"),
    path("operadores", views.operadores, name="operadores"),
    ]
