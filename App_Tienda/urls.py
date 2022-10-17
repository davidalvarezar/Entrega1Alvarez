from django.urls import path
from django import views
from App_Tienda import views
from App_Tienda.views import*
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.inicio, name = "inicio"),
    path('SobreNosotros_uno/', views.SobreNosotros_uno, name = "SobreNosotros_uno"),
    path('ckeditorSobreNosotros/', views.ckeditorSobreNosotros, name = "ckeditorSobreNosotros"),
    path('NuestrasOficinas_uno/', views.NuestrasOficinas_uno, name = "NuestrasOficinas_uno"),
    path('ckNuestrasOficinas/', views.ckNuestrasOficinas, name = "ckNuestrasOficinas"),
    path('NuestrosServicios/', views.NuestrosServicios, name = "NuestrosServicios"),
    path('ckNuestrosServicios/', views.ckNuestrosServicios, name = "ckNuestrosServicios"),
    path('login/', views.login_request, name = "login"),
    path('register/', views.register, name = "register"),
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('logout', LogoutView.as_view(template_name = 'App_Tienda/logout.html'), name = 'logout'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),


]

