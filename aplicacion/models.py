from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Moto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.marca} ({self.modelo})"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Accesorio(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    origen = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.marca}, {self.nombre}, {self.origen}"

class Taller(models.Model):
    mecanico = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()  

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"