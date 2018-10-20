from django import forms

from .models import Adoptante

class AdoptanteForm(forms.ModelForm):

    class Meta:
        model = Adoptante
        fields = ('correo', 'run', 'nombreCompleto', 'fechaNacimiento', 'telefono', 'region', 'ciudad', 'vivienda')