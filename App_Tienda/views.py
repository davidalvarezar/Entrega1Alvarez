from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render, HttpResponse
from .models import SobreNosotros, servicios, NuestrasOficinas, Avatar
from django.http import HttpResponse
from App_Tienda.forms import UserRegisterForm, UserEditForm, AvatarFormulario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def inicio(request):
    return render(request, "App_Tienda/inicio.html" )


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


def NuestrosServicios(request):
    services = servicios.objects.all()
    print(services)
    return render (request, "App_Tienda/servicios.html", {"services": services})


def contacto(request):
    return render (request, "App_Tienda/contacto.html")


def ckeditor(request):
    return render (request, "App_Tienda/inicio.html")

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid:  

                informacion = miFormulario.cleaned_data
            
                #Datos que se modificarán
                usuario.email = informacion['email']
                usuario.password1 = informacion['password1']
                usuario.password2 = informacion['password1']
                usuario.save()

                return render(request, "AppTienda/inicio.html") 
    else: 
            miFormulario= UserEditForm(initial= { 'email':usuario.email} ) 

    
    return render(request, "AppTienda/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})



@login_required
def agregarAvatar(request):
    if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES)

            if miFormulario.is_valid:

                u = User.objects.get(username=request.user)
                
                avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 

                avatar.save()

                return render(request, "AppTienda/inicio.html") #Vuelvo al inicio o a donde quieran

    else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

    return render(request, "AppTienda/agregarAvatar.html", {"miFormulario":miFormulario})


def urlImagen():

    return "/media/logo.png"

def logout(request):
    logout(request)
    return render(request, "App_Tienda/inicio.html")

