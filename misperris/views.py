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
    return render(request, 'misperris/galeria.html',{})

@login_required
def adopta(request):
    return render(request, 'misperris/adopta.html', {})
    adoptante = get_object_or_404(Adoptante)
    if request.method == "POST":
        form = PostForm(request.POST, instance=adoptante)
        if form.is_valid():
            adoptante = form.save(commit=False)
            adoptante.save()
            return redirect('adopta')
        else:
            form = PostForm(instance=adoptante)
        return render (request, 'misperris/adopta.html', {'form' : form})
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        ...
