from django.shortcuts import render
from .models import clientes
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, "App_Tienda/inicio.html" )


def presentacion(request):
    if request.method == "POST":
        cliente= clientes(nombre = request.POST["nombre"], apellido = request.POST["apellido"], email= request.POST["email"])
        cliente.save()
        return render(request, "App_Tienda/presentacion.html")
    return render(request, "App_Tienda/presentacion.html")


def sucursales(request):
    return render(request, "App_Tienda/sucursales.html")


def nosotros(request):
    return render(request, "App_Tienda/nosotros.html")