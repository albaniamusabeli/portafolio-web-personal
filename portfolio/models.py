from django.db import models

# Create your models here.

# Modelos para la base de datos

class Project(models.Model):
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to = 'Projects')
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['fechaCreacion'] # ordenar por fecha desde el mas antiguo al mas nuevo

        #ordenar por fecha desde el mas nuevo al mas antiguo
        # ordering = ['-fechaCreacion']
    
    def __str__(self):
        return self.titulo