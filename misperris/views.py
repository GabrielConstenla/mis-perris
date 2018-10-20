from django.shortcuts import render
from django.utils import timezone
from .models import Adoptante, Adoptado
from .forms import AdoptanteForm
from django.shortcuts import redirect

# Create your views here.

def index(request):
    adoptantes = Adoptante.objects.filter(fechaNacimiento=timezone.now()).order_by('fechaNacimiento')
    adoptados = Adoptado.objects.order_by('nombre')
    return render(request, 'misperris/index.html', {'adoptantes': adoptantes, 'adoptados': adoptados})

def galeria(request):
    return render(request, 'misperris/galeria.html',{})

def adopta(request):
    if request.method == "ADOPTANTE":
        form = AdoptanteForm(request.ADOPTANTE)
        if form.is_valid():
            adoptante = form.save(commit=False)
            adoptante.save()
            return redirect('misperris.views.index')
    else:
        form = AdoptanteForm()
    return render(request, 'misperris/adopta.html', {'form': form})

