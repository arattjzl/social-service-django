from django.db import models

# Create your models here.

class Instituciones(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField("Descripción", null=True, blank=True)
    direccion = models.CharField("Dirección", max_length=250)
    telefono = models.CharField(max_length=10)
    mail = models.EmailField('E-mail', max_length=254) 
    imagen = models.ImageField('Imagen', upload_to="fotos", null=True, blank=True)

    def __str__(self):
        return self.nom