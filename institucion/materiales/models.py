from django.db import models
from django.contrib.auth.models import User
from academico.models import Programa

class Material(models.Model):
    titulo = models.CharField(max_length=200)
    archivo_pdf = models.FileField(upload_to='materiales/')
    autor = models.CharField(max_length=200)
    anio = models.PositiveIntegerField()
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Material Académico"
        verbose_name_plural = "Materiales Académicos"

    def __str__(self):
        return self.titulo
