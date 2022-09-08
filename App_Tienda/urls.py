from django.urls import path

from App_Tienda.views import*

urlpatterns = [
    path("", inicio, name = "inicio"),
    path('presentacion/', presentacion, name = "presentacion"),
    path('sucursales/', sucursales, name = "sucursales"),
    path('buscar/', buscar, name = "buscar"),
    path('productosa/', productosa, name= "productosa" ),
]