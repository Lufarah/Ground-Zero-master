from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    context= {}
    return render(request, 'home/index.html', context)


def crear(request):

    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"] 

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        context= {"user": user}
        return render(request, 'home/crear-usuario.html', context)
    else:
        context= {}
        return render(request, 'home/crear-usuario.html', context)

@login_required
def ticket(request):
    context={}
    return render(request, 'home/ticket.html', context)

def inicio(request):
    context={}
    return render(request, 'home/index.html', context)

def galeria(request):
    context={}
    return render(request, 'home/Galeria.html', context)

def escultura(request):
    context={}
    return render(request, 'home/escultura.html', context)

def pintura(request):
    context={}
    return render(request, 'home/pintura.html', context)

def tejidos(request):
    context={}
    return render(request, 'home/tejido.html', context)

def orfebreria(request):
    context={}
    return render(request, 'home/orfebreria.html', context)