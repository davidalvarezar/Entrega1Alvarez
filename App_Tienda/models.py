from django.db import models

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

class sucursales(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    contacto=models.IntegerField() 