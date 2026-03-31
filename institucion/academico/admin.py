from django.contrib import admin
from .models import Carrera, Programa

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'carrera', 'fecha_creacion')
    list_filter = ('tipo', 'carrera')
    search_fields = ('nombre',)