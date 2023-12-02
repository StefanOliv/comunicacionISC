from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import registro_usuarioForm, registro_proyectoForm

def registro_usuario(request):
    if request.method == 'POST':
        registro_altausuario = registro_usuarioForm(request.POST)
        if registro_altausuario.is_valid():
            usuario = registro_altausuario.save()
            login(request, usuario)
            return redirect('/')
    else:
        registro_altausuario = registro_usuarioForm()
    return render(request, 'registro_usuario.html', {'registro_altausuario':registro_altausuario})

def registro_proyecto (request):
    if request.method == 'POST':
        registro_proyectoAlta = registro_proyectoForm (request.POST)
        if registro_proyectoAlta.is_valid():
            registro_proyectoAlta.save()
            return redirect('/')
    else:
        nuevo_usuario = registro_proyectoForm()
        registro_proyectoAlta = registro_proyectoForm()
    return render(request, 'registro_proyecto.html', {'registro_proyectoAlta': registro_proyectoAlta})   