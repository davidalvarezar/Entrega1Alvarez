from django.urls import path

from App_Tienda.views import*

urlpatterns = [
    path("", inicio, name = "inicio"),
    path('SobreNosotros/', SobreNosotros, name = "SobreNosotros"),
    path('NuestrasOficinas/', NuestrasOficinas, name = "NuestrasOficinas"),
    path('servicios/', servicios, name = "servicios"),
    path('registrarse/', registrarse, name = "registrarse"),
    path('contacto/', contacto, name = "contacto"),
    
]