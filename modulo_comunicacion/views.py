from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()

from .models import Canal_Comunicacion, Mensajes_canal, Archivopublico, Archivoprivado, MensajePrivados
from proyecto_usuario.models import registro_proyecto

from .forms import anadirCanalForm, archivopriv, archivogrupal

# --------------Vista de usuarios (mensajes directos)------------------------
def base (request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'index.html', {'users': users})
    
# -------------------------mensajes directo vista y funcionalidad-----------------------
def mensajes_directos (request, username):
    user_obj = User.objects.get(username=username)
    users = User.objects.exclude(username=request.user.username)

# ---------------Subir archivo----------------
    if request.method == 'POST':
        archivonew = archivopriv(request.POST, request.FILES)
        file = request.FILES['file']
        filenew = Archivoprivado.objects.create(filepriv=file)
        filenew.save()
        
    else:
        archivonew= archivopriv()
# ---------------------------

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
        print(thread_name)
    messaje_obj = MensajePrivados.objects.filter(thread_name=thread_name)
    return render(request, 'mensajes_direct.html', {'users': users, 'user_obj':user_obj, 'archivonew':archivonew, 'files':Archivoprivado.objects.all(), 'messages':messaje_obj})

@login_required
def CanalesAltas(request):
    canales = Canal_Comunicacion.objects.all()
    crearcanal = anadirCanalForm()
    if request.method == 'POST':
        crearcanal = anadirCanalForm(request.POST)
        if crearcanal.is_valid():
            crearcanal.save()
        else:
            crearcanal = anadirCanalForm()
    return render(request, 'canales.html', {'canales': canales, 'crearcanal':crearcanal, 'usuarios':User.objects.all(), 'proyectos':registro_proyecto.objects.all()})

@login_required
def CanalVista(request, slug):
    vistaCanal = Canal_Comunicacion.objects.get(slug=slug)
    mensajesenviados = Mensajes_canal.objects.filter(canal=vistaCanal)[0:25]
    return render(request, 'vista_canal.html', {'vistaCanal': vistaCanal,'mensajesenviados':mensajesenviados})