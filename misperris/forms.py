from django import forms
from .models import Adoptante
from django.core.exceptions import ValidationError



class AdoptanteForm(forms.ModelForm):

    class Meta:
        model = Adoptante
        fields = ('correo', 'run', 'nombreCompleto', 'telefono','region','vivienda')

    def clean_correo(self):
        correo = self.cleaned_data['correo']

        correo_base, proveedor = correo.split("@")
        dominio, extension = proveedor.split(".")
        if not dominio == "gmail":
            raise ValidationError("Se tiene que registrar con un correo gmail.com")
        elif not extension == "com":
            raise ValidationError("Se tiene que registrar con un correo gmail.com")
        return correo


    def clean_run(self):
        run = self.cleaned_data['run']
        if not "-" in run:
            raise ValidationError("Digita tu run sin puntos pero con guión")
        elif len(run) <= 8:
            raise ValidationError("Ingresa un run con un mínimo de 9 caracteres")
        # elif run.isalpha() == "k":
        #     raise ValidationError("Debe ingresar un run con k")
        return run

    def clean_nombreCompleto(self):
        nombreCompleto = self.cleaned_data['nombreCompleto']
        if len(nombreCompleto.split(' ')) < 4 :
            raise ValidationError("Por favor ingresa tu nombre completo")
        return nombreCompleto

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if telefono.isalpha():
            raise ValidationError('El teléfono no puede contener letras')
        elif len(telefono) <= 8:
            raise ValidationError("Ingresa un teléfono con un 9 digitos")
        return telefono

  