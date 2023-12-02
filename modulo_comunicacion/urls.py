from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('favicon.ico/', RedirectView.as_view(url='/static/img/favicon/favicon.ico')),
    path('', views.CanalesAltas, name='canales' ),
    path('<slug:slug>', views.CanalVista, name='canalesVista' ),
]