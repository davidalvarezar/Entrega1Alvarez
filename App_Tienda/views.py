from multiprocessing import AuthenticationError
from re import A
from django.shortcuts import redirect, render, HttpResponse
from .models import productos, Avatar
from django.http import HttpResponse
from App_Tienda.forms import UserRegisterForm, UserEditForm, AvatarFormulario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@login_required
def inicio(request):
    lista = Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar = lista[0].imagen.url
    else:
        avatar=""
    
    return render (request, "App_Tienda/inicio.html" , {"avatar":obtenerAvatar(request)})

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
    return render (request, "App_Tienda/register.html", {"form":form , "avatar":obtenerAvatar(request)})

def SobreNosotros(request):
    return render (request, "App_Tienda/SobreNosotros.html", {"avatar":obtenerAvatar(request)})

def NuestrasOficinas(request):
    return render (request, "App_Tienda/NuestrasOficinas.html", {"avatar":obtenerAvatar(request)})

def servicios(request):
    return render (request, "App_Tienda/servicios.html", {"avatar":obtenerAvatar(request)})

def contacto(request):
    return render (request, "App_Tienda/contacto.html", {"avatar":obtenerAvatar(request)})

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

    
    return render(request, "AppTienda/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario , "avatar":obtenerAvatar(request)})



@login_required
def agregarAvatar(request):
        if request.method == 'POST':
                miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid:
            avatarViejo=Avatar.objects.filter(user=request.user)
            if (len(avatarViejo)>0):
                avatarViejo[0].delete()
            avatar = Avatar (user=request.user, imagen=miFormulario.cleaned_data['imagen']) 
            avatar.save()

            return render(request, "AppTienda/inicio.html", {'usuario':request.user, 'mensaje':'AVATAR AGRAGADO', "imagen":avatar.imagen.url}) 

        else: 

            miFormulario= AvatarFormulario() 

        return render(request, "AppTienda/agregarAvatar.html", {"miFormulario":miFormulario, "avatar":obtenerAvatar(request)} )

def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user.id)
    if len(lista) != 0:
        imagen=lista[0].imagen.url
    else:
        imagen=""
    return imagen


def urlImagen():

    return "/media/logo.png"

def logout(request):
    logout(request)
    return render(request, "App_Tienda/inicio.html")

