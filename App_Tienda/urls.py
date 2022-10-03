from django.urls import path

from App_Tienda.views import*

urlpatterns = [
    path("", inicio, name = "inicio"),
    path('SobreNosotros/', SobreNosotros, name = "SobreNosotros"),
    path('NuestrasOficinas/', NuestrasOficinas, name = "NuestrasOficinas"),
    path('servicios/', servicios, name = "servicios"),
    path('contacto/', contacto, name = "contacto"),
    path('ckeditor/', ckeditor, name = "ckeditor"),
    path('register/', register, name = "register"),
    path('login/', login_request, name = "login"),

]