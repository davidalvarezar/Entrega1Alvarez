from django.urls import path

from App_Tienda.views import presentacion

urlpatterns = [
    path('presentacion/', presentacion ),
]