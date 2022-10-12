from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class SobreNosotros(models.Model):
    titulo = RichTextField(max_length=200)
    subtitulo = RichTextField(max_length=20000)
    cuerpo = RichTextField(max_length=20000)
    autor = RichTextField(max_length=200)
    imagen = RichTextField(max_length=200)
    fecha = models.DateTimeField()
    

class servicios(models.Model):
    titulo = RichTextField(max_length=200000)
    subtitulo = RichTextField(max_length=200000)
    cuerpo = RichTextField(max_length=200000000)
    autor = RichTextField(max_length=200)
    imagen = RichTextField(max_length=200)
    fecha = models.DateTimeField()
    

class NuestrasOficinas(models.Model):
    titulo = RichTextField(max_length=200000)
    subtitulo = RichTextField(max_length=200000)
    cuerpo = RichTextField(max_length=200000)
    autor = RichTextField(max_length=200)
    imagen = RichTextField(max_length=200)
    fecha = models.DateTimeField()


class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"


