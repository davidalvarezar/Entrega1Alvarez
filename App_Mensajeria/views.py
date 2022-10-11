from django.shortcuts import render
from .models import emisor, receptor, Canalmensajes
from django.http import HttpResponse
from App_Mensajeria.forms import FormMensajes
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required
def enviarMensajes(request):
    usuario = request.user  #usuario ya registrado y logueado
    if request.method=="POST":
        pass
    
        




@login_required
def leerMensajes(request):
    return HttpResponse("Mensaje Leído")

@login_required
def responderMensajes(request):
    return HttpResponse("Responder Mensajes")

@login_required
def mensajeFormulario(request):
    if request.method =="POST":
        form = FormMensajes(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            mensaje = info["mensaje"]
            
            contenido_mensaje = emisor(mensaje=mensaje)
            contenido_mensaje.save()
            return render (request, "App_Mensajeria/mensajesForm.html")
    else:
        form = FormMensajes()
    return render (request, "App_Mensajeria/mensajesForm.html", {"formulario": form})



