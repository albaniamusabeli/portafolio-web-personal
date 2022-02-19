from django.db import models

# Create your models here.

# Modelos para la base de datos

class Project(models.Model):
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)