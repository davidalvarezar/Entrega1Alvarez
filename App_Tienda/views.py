from django.shortcuts import render
from .models import clientes
# Create your views here.

def inicio(request):
    return render(request, "App_Tienda/inicio.html" )


def presentacion(request):
    nombre = clientes.objects.all()
    apellido = clientes.objects.all()
    email = clientes.objects.all()

    return render(request, "App_Tienda/presentacion.html", {"nombreC": nombre, "apellidoC": apellido, "emailC": email})


def sucursales(request):
    return render(request, "App_Tienda/sucursales.html")


def nosotros(request):
    return render(request, "App_Tienda/nosotros.html")