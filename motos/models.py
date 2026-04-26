from django.db import models
from ckeditor.fields import RichTextField

class Moto(models.Model):
    # Los 2 CharField requeridos
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    
    # Texto enriquecido para la reseña o descripción
    descripcion = RichTextField(blank=True, null=True)
    
    # Campo de imagen (se guardarán en la carpeta /media/motos/)
    imagen = models.ImageField(upload_to='motos', blank=True, null=True)
    
    # Campo de fecha automático
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca} {self.modelo}"
