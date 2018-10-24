from django.core.exceptions import ValidationError

def run_validation(value):
    if not "-":
        raise ValidationError('ingrese su rut con guion porfavor')