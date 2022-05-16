from django.db import models
from django.forms import IntegerField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="producto", null=True)
    

    def __str__(self):
        return self.nombre