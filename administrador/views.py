from django.shortcuts import render
from clientes.models import Cliente
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def menu(request):
    request.session["usuario"]="luci"
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'administrador/menu.html', context)


def quienes_somos(request):
    request.session["usuario"]="jazocar"
    usuario=request.session["usuario"]
    context= {'usuario':usuario}
    return render(request, 'administrador/quienes_somos.html', context)


def home(request):
    context = {}
    return render(request, 'administrador/home.html', context)