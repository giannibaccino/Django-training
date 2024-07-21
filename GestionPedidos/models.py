from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    
class Articulos(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField()
    
class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateTimeField()
    entregado = models.BooleanField()