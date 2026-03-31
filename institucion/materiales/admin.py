from django.contrib import admin
from .models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'programa', 'autor', 'anio', 'fecha_subida')
    list_filter = ('programa', 'anio')
    search_fields = ('titulo', 'autor')
    date_hierarchy = 'fecha_subida'
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.creado_por = request.user
        super().save_model(request, obj, form, change)