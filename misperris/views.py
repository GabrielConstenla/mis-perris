from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Adoptante, Adoptado
from .forms import AdoptanteForm, AdoptadoForm
from django.shortcuts import redirect


# PARA INICIO DE SESION
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def index(request):
    adoptantes = Adoptante.objects.order_by('run')
    adoptados = Adoptado.objects.order_by('nombre')
    return render(request, 'misperris/index.html', {'adoptantes': adoptantes, 'adoptados': adoptados})

def galeria(request):
    pDisponibles = Adoptado.objects.filter(estado__contains='Disponible')
    pRescatados = Adoptado.objects.filter(estado__contains='Rescatado')
    pAdoptados = Adoptado.objects.filter(estado__contains='Adoptado')
    return render(request, 'misperris/galeria.html',{'pDisponibles': pDisponibles, 'pAdoptados': pAdoptados ,'pRescatados': pRescatados})


@login_required
def adopta(request):
    if request.method == "POST":
        form = AdoptanteForm(request.POST)
        if form.is_valid():
            Adoptante = form.save(commit=False)
            Adoptante.save()
            return redirect('perritos_disponibles')
    else:
        form = AdoptanteForm()
    return render(request, 'misperris/adopta.html',{'form': form})


def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        ...

@login_required
def perritos_disponibles(request):
    pDisponibles = Adoptado.objects.filter(estado__contains='Disponible')
    return render(request, 'misperris/galeriaDisponible.html', {'pDisponibles': pDisponibles})

def perritos_rescatados(request):
    pRescatados = Adoptado.objects.filter(estado__contains='Rescatado')
    return render(request, 'misperris/galeriaRescatado.html', {'pRescatados': pRescatados})

def perritos_adoptados(request):
    pAdoptados = Adoptado.objects.filter(estado__contains='Adoptado')
    return render(request, 'misperris/galeriaAdoptado.html', {'pAdoptados': pAdoptados})

@login_required
def detalle_perro(request, pk):
    adoptado = get_object_or_404(Adoptado, pk=pk)
    return render(request, 'misperris/detalle_perro.html',{'adoptado': adoptado})

@login_required
def adoptar_perro(request, pk):
    adoptado = get_object_or_404(Adoptado, pk=pk)
    if request.method == "POST":
        form = AdoptadoForm(request.POST, instance=adoptado)
        if form.is_valid():
            adoptado = form.save(commit=False)
            adoptado.save()
            return redirect('galeria')
    else:
        form = AdoptadoForm(instance=adoptado)
    return render(request, 'misperris/adoptar_perro.html', {'form': form, 'adoptado': adoptado})
