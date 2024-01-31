from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('crear-usuario', views.crear, name='crear-usuario'),
    path('ticket', views.ticket, name='ticket'),
    path('inicio',views.inicio, name='inicio'),
    path('galeria', views.galeria, name='galeria'),
    path('escultura', views.escultura, name='escultura'),
    path('pintura', views.pintura, name='pintura'),
    path('tejidos', views.tejidos, name='tejidos'),
    path('orfebreria', views.orfebreria, name='orfebreria'),

   ]