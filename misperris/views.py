from django.shortcuts import render
from django.utils import timezone
from .models import Adoptante, Adoptado

# PARA INICIO DE SESION
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def index(request):
    adoptantes = Adoptante.objects.filter(fechaNacimiento=timezone.now()).order_by('fechaNacimiento')
    adoptados = Adoptado.objects.order_by('nombre')
    return render(request, 'misperris/index.html', {'adoptantes': adoptantes, 'adoptados': adoptados})

def galeria(request):
    return render(request, 'misperris/galeria.html',{})

@login_required
def adopta(request):
    return render(request, 'misperris/adopta.html', {})

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        ...
