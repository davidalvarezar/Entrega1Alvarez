from unittest.util import _MAX_LENGTH
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

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


