from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import path, include
from proyecto_usuario.views import registro_usuario,registro_proyecto
from modulo_comunicacion.views import base, mensajes_directos

from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico/', RedirectView.as_view(url='/static/img/favicon/favicon.ico')),
    path('canales/', include('modulo_comunicacion.urls')),
    path('', base, name='index'),
    path('<str:username>', mensajes_directos, name='msg'),
    path('registro_usuario/', registro_usuario, name='registro_usuario' ),
    path('registro_proyecto/', registro_proyecto, name='registro_proyecto' ),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout' ),
]
