from django.urls import path
from django import views
from App_Tienda import views
from App_Tienda.views import*
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", inicio, name = "inicio"),
    path('SobreNosotros/', SobreNosotros, name = "SobreNosotros"),
    path('NuestrasOficinas/', NuestrasOficinas, name = "NuestrasOficinas"),
    path('servicios/', servicios, name = "servicios"),
    path('contacto/', contacto, name = "contacto"),
    path('login/', login_request, name = "login"),
    path('register/', register, name = "register"),
    path('login', login_request, name = 'Login'),
    path('register', register, name = 'Register'),
    path('editarPerfil', editarPerfil, name="EditarPerfil"),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    path('logout', LogoutView.as_view(template_name = 'App_Tienda/logout.html'), name = 'Logout'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)