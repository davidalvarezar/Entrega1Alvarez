from django.urls import path
from django import views
from App_Mensajeria.views import*

urlpatterns = [
    path("", enviarMensajes),
    path("leer", leerMensajes),
    path("responder", responderMensajes),
    path("mensajeFormulario", mensajeFormulario, name="mensajeFormulario"),

]