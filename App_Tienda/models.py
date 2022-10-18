from unittest.util import _MAX_LENGTH
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class productos (models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.CharField(max_length=50)
    precio=models.IntegerField()
    def __str__(self) -> str:
        return self.nombre+""+self.categoria+""+str(self.precio)

class clientes(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self) -> str:
        return self.nombre+""+self.apellido+""+self.email


class SobreNosotros(models.Model):
    titulo = RichTextField(max_length=200)
    subtitulo = RichTextField(max_length=200)
    cuerpo = RichTextField(max_length=20000)
    autor = RichTextField(max_length=200)
    fecha = RichTextField(max_length=200)
    imagen = RichTextField(max_length=200)
    


class servicios(models.Model):
    titulo = RichTextField(max_length=200)
    subtitulo = RichTextField(max_length=200)
    cuerpo = RichTextField(max_length=20000)
    autor = RichTextField(max_length=200)
    fecha = RichTextField(max_length=200)
    imagen = RichTextField(max_length=200)

class NuestrasOficinas(models.Model):
    titulo = RichTextField(max_length=200)
    subtitulo = RichTextField(max_length=200)
    cuerpo = RichTextField(max_length=20000)
    autor = RichTextField(max_length=200)
    fecha = RichTextField(max_length=200)
    imagen = RichTextField(max_length=200)

class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares')

    def __str__(self):
        return f"Imagen de: {self.user.username}"


class Nosotros(models.Model):
    titulo = RichTextField(max_length=20000)
    subtitulo = RichTextField(max_length=20000)
    cuerpo = RichTextField(max_length=200000)
    autor = RichTextField(max_length=2000)
    imagen = RichTextField(max_length=200)
    fecha = models.DateTimeField()

class services(models.Model):
    titulo = RichTextField(max_length=200000)
    subtitulo = RichTextField(max_length=200000)
    cuerpo = RichTextField(max_length=200000000)
    autor = RichTextField(max_length=20000)
    imagen = RichTextField(max_length=200)
    fecha = models.DateTimeField()

class Oficinas(models.Model):
    titulo = RichTextField(max_length=200000)
    subtitulo = RichTextField(max_length=200000)
    cuerpo = RichTextField(max_length=200000)
    autor = RichTextField(max_length=2000)
    imagen = RichTextField(max_length=200)
    fecha = models.DateTimeField()



