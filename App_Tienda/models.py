from unittest.util import _MAX_LENGTH
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Nosotros(models.Model):
    titulo = RichTextField(max_length=20000)
    subtitulo = RichTextField(max_length=20000)
    cuerpo = RichTextField(max_length=200000)
    autor = RichTextField(max_length=2000)
    imagen = RichTextField(max_length=20000000)
    fecha = models.DateTimeField()

class services(models.Model):
    titulo = RichTextField(max_length=200000)
    subtitulo = RichTextField(max_length=200000)
    cuerpo = RichTextField(max_length=200000000)
    autor = RichTextField(max_length=20000)
    imagen = RichTextField(max_length=200000)
    fecha = models.DateTimeField()

class Oficinas(models.Model):
    titulo = RichTextField(max_length=200000)
    subtitulo = RichTextField(max_length=200000)
    cuerpo = RichTextField(max_length=200000)
    autor = RichTextField(max_length=2000)
    imagen = RichTextField(max_length=2000000)
    fecha = models.DateTimeField()


class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares')

    def __str__(self):
        return f"Imagen de: {self.user.username}"


