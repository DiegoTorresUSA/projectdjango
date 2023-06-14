from django import forms
from .models import Concesionario


class ConcesionarioForm(forms.ModelForm):
    class Meta:
        model = Concesionario
        fields = '__all__'
        

