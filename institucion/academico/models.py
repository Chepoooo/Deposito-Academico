# Create your models here.
from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"

    def __str__(self):
        return self.nombre


class Programa(models.Model):
    TIPO_CHOICES = (
        ('MAESTRIA', 'Maestría'),
        ('ESPECIALIZACION', 'Especialización'),
    )

    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Programa Académico"
        verbose_name_plural = "Programas Académicos"

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
