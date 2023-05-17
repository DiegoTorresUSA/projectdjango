from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:operador_id>/", views.detalle, name="Operador"),
    path("<int:operador_id>/vehiculos", views.vehiculos, name="Vehiculos"),
    ]
