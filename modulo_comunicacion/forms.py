from django.forms import ModelForm
from django import forms
from .models import Canal_Comunicacion

class anadirCanalForm(ModelForm):           
    class Meta:
        model = Canal_Comunicacion
        fields = ['nombrecanal', 'estatus_canal', 'slug', 'fk_proyecto', 'fk_usuario']
        help_texts = {k:"" for k in fields}

class archivopriv (forms.Form):
    file = forms.FileField()

class archivogrupal (forms.Form):
    file = forms.FileField()