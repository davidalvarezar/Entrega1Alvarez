from django.urls import path

from App_Tienda.views import*

urlpatterns = [
    path("", inicio, name = "inicio"),
    path('presentacion/', presentacion, name = "presentacion"),
]