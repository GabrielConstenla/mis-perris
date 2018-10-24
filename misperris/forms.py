from django import forms

from .models import Adoptante

class AdoptanteForm(forms.ModelForm):

    class Meta:
        model = Adoptante
        fields = ('correo', 'run', 'nombreCompleto', 'telefono',)

    def run_validator(self):
        run = cleaned_data.get("run")
        if not "-" in run:
            raise forms.ValidatorError("Por favor ponle un ( - ) a tu wea")
        return run