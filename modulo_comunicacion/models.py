from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from proyecto_usuario.models import registro_proyecto

class Canal_Comunicacion(models.Model):
    estatus_choice = (
        ("ABIERTO", "Abierto"), 
        ("CERRADO", "Cerrado"), 
    )
    nombrecanal = models.CharField(max_length=25)
    fecha_crecion_canal = models.DateTimeField(default=datetime.now, blank=True)
    estatus_canal = models.CharField(max_length=15, choices=estatus_choice, default="Abierto")
    slug = models.SlugField(unique=True)
    fk_proyecto = models.ForeignKey(registro_proyecto, on_delete=models.CASCADE)
    fk_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombrecanal

    class Meta:
        db_table = 'Canal_Comunicacion'
        verbose_name = 'Canal_Comunicacion'
        verbose_name_plural = 'Canales_Comunicacion'

class Mensajes_canal(models.Model):
    canal = models.ForeignKey(Canal_Comunicacion, related_name='mensajesCanal', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='mensajesCanal', on_delete=models.CASCADE)
    contenido = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

class Archivos (models.Model):
    mensajes_canal = models.ForeignKey(Mensajes_canal, on_delete=models.CASCADE)
    file = models.FileField(upload_to='archivos/canales')

    class Meta:
        db_table = 'Arhivos'
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'

class MensajePrivados (models.Model):
    sender = models.CharField(max_length=100, default=None)
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    archivopriv= models.FileField(upload_to='media/',  blank=False, null=True)

    def __str__(self):
        return self.message

class Archivoprivado (models.Model):
    thread_name = models.CharField(null=True, blank=True, max_length=50)
    filepriv = models.FileField(upload_to='archivos/privados', blank=False, null=True)

class Archivopublico (models.Model):
    
    filegroup = models.FileField(upload_to='archivos/grupales', blank=False, null=True)