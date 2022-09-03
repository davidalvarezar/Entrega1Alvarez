from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class productos (models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.CharField(max_length=50)
    precio=models.IntegerField()

class clientes(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

class sucursales(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    contacto=models.IntegerField() 