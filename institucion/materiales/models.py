from email.policy import default
from time import timezone
from django.db import models
from django.contrib.auth.models import User
from institucion.academico.models import Programa

class Material(models.Model):

    titulo = models.CharField(max_length=300)
    autor = models.CharField(max_length=300)
    anio = models.PositiveIntegerField()

    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)

    posgrado = models.CharField(max_length=200)
    instituto = models.CharField(max_length=300)
    area_conocimiento = models.CharField(max_length=200)
    linea_investigacion = models.CharField(max_length=200)

    resumen = models.TextField()

    palabras_clave = models.CharField(
        max_length=300,
        help_text="Separadas por comas"
    )

    archivo_pdf = models.FileField(upload_to='materiales/')

    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
