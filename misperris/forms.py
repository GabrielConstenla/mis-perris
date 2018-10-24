from django import forms
from .models import Adoptante
from django.core.exceptions import ValidationError



class AdoptanteForm(forms.ModelForm):

    class Meta:
        model = Adoptante
        fields = ('correo', 'run', 'nombreCompleto', 'telefono',)

    def clean_run(self):
        run = self.cleaned_data['run']
        if not "-" in run:
            raise ValidationError("Digita tu run sin puntos pero con guión")
        # elif len(run.split()) <= 8:
        #     raise ValidationError("Ingresa un rut con un minimo de 9 caracteres")
        # if len(run.split()) <= 8:
        #     raise ValidationError("Ingresa un rut con un minimo de 9 caracteres")
        return run

    def clean_largo_run(self):
        run= self.cleaned_data['run']
        if len(run.split()) <= 8:
            raise ValidationError("Ingresa un rut con un minimo de 9 caracteres")
        return run

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if telefono.isalpha():
            raise ValidationError('El telefono no puede contener letras')
        # if len(telefono.split()) <= 8:
        #     raise ValidationError("Ingresa un telefono con un 9 digitos")
        return telefono
  