
from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import  User

class FormSobreNosotros(forms.Form):
    ingreso = forms.CharField(label="Ingresar")


class FormNuestrasOficinas(forms.Form):
    ingreso = forms.CharField(label="Ingresar")


class FormNuestrosServicios(forms.Form):
    ingreso = forms.CharField(label="Ingresar")

    
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario", max_length=50)
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)



    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    username = forms.CharField(label="Nuevo nombre de usuario", max_length=50)
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    first_name=forms.CharField(label="Modificar Nombre")
    last_name=forms.CharField(label="Modificar Apellido")


    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name', 'username' ] 
        help_texts = {k:"" for k in fields}



class AvatarForm(forms.Form):
    
    imagen = forms.ImageField(label="Imagen")