from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = RichTextField(max_length=20000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Autor')
    fecha = models.DateField(null=True, blank=True, verbose_name='Fecha publicación del post')
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True) 

    def __str__(self):
        return f'Título: {self.titulo} -- Autor: {self.user}'


# Para comentar las publicaciones
'''class Comment(models.Model): 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    nombre = models.CharField(max_length=50)
    comentario = models.TextField(max_length=200)
    fecha = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Nombre: {self.nombre} -- Comentario: {self.comentario} -- Fecha: {self.fecha}'''''