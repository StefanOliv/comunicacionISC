from django.contrib import admin
from .models import Canal_Comunicacion, MensajePrivados, Archivos, Archivoprivado, Archivopublico

admin.site.register(Canal_Comunicacion)
admin.site.register(MensajePrivados)
admin.site.register(Archivos)
admin.site.register(Archivoprivado)
admin.site.register(Archivopublico)
