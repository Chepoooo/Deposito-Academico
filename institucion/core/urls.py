from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carreras/', views.lista_carreras, name='carreras'),
    path('carreras/<int:carrera_id>/programas/', views.programas_por_carrera, name='programas'),
    path('programas/<int:programa_id>/materiales/', views.materiales_por_programa, name='materiales'),
    path('buscador/', views.buscador, name='buscador'),
    path('material/<int:material_id>/', views.detalle_material, name='detalle_material'),
    path('carrera/<int:carrera_id>/programas/', views.programas, name='programas'),

]
