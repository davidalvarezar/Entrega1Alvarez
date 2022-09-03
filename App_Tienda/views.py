from django.shortcuts import render
from .models import clientes
# Create your views here.

def presentacion(request):
    nombre=clientes.objects.all()
    apellido=clientes.objects.all()
    email=clientes.objects.all()
    return render(request, "index.html", {"nombreC":nombre, "apellidoC":apellido, "emailC":email})
