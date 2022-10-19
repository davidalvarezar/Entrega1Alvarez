from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render, HttpResponse
from .models import Nosotros, Oficinas, Avatar, services
from django.http import HttpResponse
from App_Tienda.forms import UserRegisterForm, UserEditForm, AvatarForm, FormNuestrasOficinas, FormSobreNosotros, FormNuestrosServicios
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def inicio(request):

    return render(request, "App_Tienda/inicio.html", {"avatar": obtenerAvatar(request)})

# def buscar(request):
#     if request.method == "POST":
#         nombre = request.POST["nombre"]
#         if productos.objects.filter(nombre__contains=nombre):
#             producto = productos.objects.filter(nombre__contains=nombre)
#             return render(request,"App_Tienda/buscar.html",{"productos":producto})
#         else:
#             return HttpResponse("material no encontrado")
#     return render(request, "App_Tienda/buscar.html")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, "App_Tienda/inicio.html", {"Mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "App_Tienda/inicio.html")
        else:
            return render(request, "App_Tienda/inicio.html", {"Mensaje": "Usuario o contraseña incorrectos"})
    else:
        form = AuthenticationForm()
        return render(request, "App_Tienda/login.html", {"form": form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, "App_Tienda/inicio.html", {"Mensaje": f"Bienvenido {username}"})
        else:
            return render(request, "App_Tienda/register.html", {"form": form, "Mensaje": "Error al registrar"})
    else:
        form = UserRegisterForm()
    return render(request, "App_Tienda/register.html", {"form": form})

def SobreNosotros_uno(request):
    return render (request, "App_Tienda/SobreNosotros_uno.html", {"avatar": obtenerAvatar(request)})


def ckeditorSobreNosotros(request):
    nosotros = Nosotros.objects.all()
    return render(request, "App_Tienda/ckeditorsobrenosotros.html", {"nosotros": nosotros})

    

def NuestrasOficinas_uno(request):
    return render (request, "App_Tienda/NuestrasOficinas.html", {"avatar": obtenerAvatar(request)})


def ckNuestrasOficinas(request):
    ofi = Oficinas.objects.all()
    return render (request, "App_Tienda/ckeditornuestrasoficinas.html", {"ofi": ofi})
    

def NuestrosServicios(request):
    return render (request, "App_Tienda/servicios.html", {"avatar": obtenerAvatar(request)})


def ckNuestrosServicios(request):
    serv = services.objects.all()
    return render(request, "App_Tienda/ckNuestrosServicios.html", {"serv":serv})


def SobreNosotros(request):
    return render(request, "App_Tienda/SobreNosotros.html", {"avatar": obtenerAvatar(request)})


def NuestrasOficinas(request):
    return render(request, "App_Tienda/NuestrasOficinas.html", {"avatar": obtenerAvatar(request)})


def servicios(request):
    return render(request, "App_Tienda/servicios.html", {"avatar": obtenerAvatar(request)})


def contacto(request):
    return render(request, "App_Tienda/contacto.html", {"avatar": obtenerAvatar(request)})


def ckeditor(request):
    return render(request, "App_Tienda/inicio.html")


@login_required
def editarPerfil(request):

    return render (request, "App_Tienda/inicio.html" )

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo = Avatar.objects.filter(user=request.user)
            if (len(avatarViejo) > 0):
                avatarViejo.delete()

            avatar = Avatar(user=request.user,
                            imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'App_Tienda/inicio.html', {'usuario': request.user, 'mensaje': 'AVATR AGREGADO EXITOSAMENTE', "imagen": avatar.imagen.url})
        else:
            return render(request, 'App_Tienda/agregarAvatar.html', {'formulario': formulario, 'mensaje': 'FORMULARIO INVALIDO'})

    else:
        formulario = AvatarForm()
        return render(request, "App_Tienda/agregarAvatar.html", {"formulario": formulario, "usuario": request.user, "avatar": obtenerAvatar(request)})


def obtenerAvatar(request):
    lista = Avatar.objects.filter(user=request.user.id)
    if len(lista) != 0:
        imagen=lista[0].imagen.url
    else:
        imagen = "/media/avatares/logopordefecto.png"
    return imagen


def urlImagen():

    return "/media/logo1.png"


def logout(request):
    return render(request, "App_Tienda/inicio.html")

