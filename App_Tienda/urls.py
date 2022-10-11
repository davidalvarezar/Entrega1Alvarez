from django.urls import path
from django import views
from App_Tienda import views
from App_Tienda.views import*
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.inicio, name = "inicio"),
    path('SobreNosotros/', views.SobreNosotros, name = "SobreNosotros"),
    path('NuestrasOficinas/', views.NuestrasOficinas, name = "NuestrasOficinas"),
    path('NuestrosServicios/', views.NuestrosServicios, name = "NuestrosServicios"),
    path('contacto/', views.contacto, name = "contacto"),
    path('login/', views.login_request, name = "login"),
    path('register/', views.register, name = "register"),
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    path('logout', LogoutView.as_view(template_name = 'App_Tienda/logout.html'), name = 'Logout'),


]