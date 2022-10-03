from multiprocessing import AuthenticationError
from django.shortcuts import render

from App_Tienda.forms import UserRegisterForm
from .models import clientes, productos
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.

def inicio(request):
    return render(request, "App_Tienda/inicio.html" )

def buscar(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        if productos.objects.filter(nombre__contains=nombre):
            producto = productos.objects.filter(nombre__contains=nombre)
            return render(request,"App_Tienda/buscar.html",{"productos":producto})
        else:    
            return HttpResponse("material no encontrado")
    return render(request, "App_Tienda/buscar.html")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, "App_Tienda/inicio.html", {"Mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "App_Tienda/login.html")
        else:    
            return render(request, "App_Tienda/login.html")
    form = AuthenticationForm()
    return render(request, "App_Tienda/login.html", {"form":form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, "App_Tienda/register.html")
    else:
        form = UserRegisterForm()
    return render(request, "App_Tienda/register.html", {"form":form})

def SobreNosotros(request):
    return render (request, "App_Tienda/SobreNosotros.html")

def NuestrasOficinas(request):
    return render (request, "App_Tienda/NuestrasOficinas.html")

def servicios(request):
    return render (request, "App_Tienda/servicios.html")

def contacto(request):
    return render (request, "App_Tienda/contacto.html")

def ckeditor(request):
    return render (request, "App_Tienda/inicio.html")

