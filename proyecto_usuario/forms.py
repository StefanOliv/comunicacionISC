from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import registro_proyecto

class registro_usuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class registro_proyectoForm (ModelForm):
     nombreproyecto = forms.CharField(label='Nombre proyecto', max_length = 50)
     descripcionProyecto = forms.CharField(label='Descripcion proyecto', max_length= 80, widget=forms.Textarea)

     class Meta:
        model = registro_proyecto
        fields = ['nombreproyecto', 'descripcionProyecto', 'fk_user']