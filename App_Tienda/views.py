from django.shortcuts import render
from .models import clientes, productos
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, "App_Tienda/inicio.html" )


'''def presentacion(request):
    if request.method == 'POST':
        cliente= clientes(nombre = request.POST["nombre"], apellido = request.POST["apellido"], email= request.POST["email"])
        cliente.save()
        return render(request, "App_Tienda/presentacion.html")
    return render(request, "App_Tienda/presentacion.html")'''

def SobreNosotros(request):
    return render (request, "App_Tienda/SobreNosotros.html")



def NuestrasOficinas(request):
    return render(request, "App_Tienda/NuestrasOficinas.html")


def servicios(request):
    return render(request, "App_Tienda/servicios.html")


def registrarse(request):
    return render(request, "App_Tienda/registarse.html")
    

def contacto(request):
    return render (request, "App_Tienda/contacto.html")


'''def buscar(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        if productos.objects.filter(nombre__contains=nombre):
            producto = productos.objects.filter(nombre__contains=nombre)
            return render(request,"App_Tienda/buscar.html",{"productos":producto})
        else:    
            return HttpResponse("material no encontrado")
    return render(request, "App_Tienda/buscar.html")'''

'''def productosa(request):
    if request.method == 'POST':
        producto= productos(nombre = request.POST["nombre"], categoria = request.POST["categoria"], precio= request.POST["precio"])
        producto.save()
        return render(request, "App_Tienda/productosa.html")
    return render(request, "App_Tienda/productosa.html")'''   

