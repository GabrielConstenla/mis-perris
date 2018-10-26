from django.shortcuts import render, get_object_or_404
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
    pDisponibles = Adoptado.objects.filter(estado__contains='Disponible')
    pRescatados = Adoptado.objects.filter(estado__contains='Rescatado')
    pAdoptados = Adoptado.objects.filter(estado__contains='Adoptado')
    return render(request, 'misperris/galeria.html',{'pDisponibles': pDisponibles, 'pAdoptados': pAdoptados ,'pRescatados': pRescatados})


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


def perritos_disponibles(request):
    pDisponibles = Adoptado.objects.filter(estado__contains='Disponible')
    return render(request, 'misperris/galeriaDisponible.html', {'pDisponibles': pDisponibles})

def perritos_rescatados(request):
    pRescatados = Adoptado.objects.filter(estado__contains='Rescatado')
    return render(request, 'misperris/galeriaRescatado.html', {'pRescatados': pRescatados})

def perritos_adoptados(request):
    pAdoptados = Adoptado.objects.filter(estado__contains='Adoptado')
    return render(request, 'misperris/galeriaAdoptado.html', {'pAdoptados': pAdoptados})
