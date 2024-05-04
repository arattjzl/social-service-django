from django.db import models

# Create your models here.

class UnidadAcademica(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField('Description')
    
    def __str__(self) -> str:
        return self.nombre

class ProgramaAcademico(models.Model):
    unidad_academica = models.ForeignKey('programa_academico.UnidadAcademica', verbose_name='Unidad Academica', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField('Description')

    def __str__(self) -> str:
        return self.nombre
