from django.shortcuts import render
from django.utils import timezone
from .models import Adoptante, Adoptado

# Create your views here.

def index(request):
    adoptantes = Adoptante.objects.filter(fechaNacimiento=timezone.now()).order_by('fechaNacimiento')
    adoptados = Adoptado.objects.order_by('nombre')
    return render(request, 'misperris/index.html', {'adoptantes': adoptantes, 'adoptados': adoptados})

def galeria(request):
    return render(request, 'misperris/galeria.html',{})

def adopta(request):
    return render(request, 'misperris/adopta.html', {})
