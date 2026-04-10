from django.shortcuts import render
from django.db.models import Q
from institucion.academico.models import Carrera, Programa
from institucion.materiales.models import Material
from django.shortcuts import get_object_or_404

from django.core.paginator import Paginator

def clean_param(value):
    return value if value not in ["", "None", None] else None


def buscador(request):

    query = request.GET.get('q', '').strip()
    programa_id = request.GET.get('programa')
    posgrado = request.GET.get('posgrado', '').strip()
    anio = request.GET.get('anio', '').strip()
    orden = request.GET.get('orden')

    materiales = Material.objects.all()

    # 🔍 BUSCADOR PRINCIPAL
    if query:
        palabras = query.split()
        filtro = Q()

        for palabra in palabras:
            filtro |= (
                Q(titulo__icontains=palabra) |
                Q(autor__icontains=palabra) |
                Q(resumen__icontains=palabra) |
                Q(palabras_clave__icontains=palabra)
            )

        materiales = materiales.filter(filtro)

    # 🎓 FILTRO PROGRAMA
    if programa_id and programa_id != "None":
        materiales = materiales.filter(programa_id=programa_id)

    # 🧠 BUSCADOR INTELIGENTE (antes "Ej: Maestría")
    if posgrado:
        materiales = materiales.filter(
            Q(programa__nombre__icontains=posgrado) |
            Q(area_conocimiento__icontains=posgrado) |
            Q(linea_investigacion__icontains=posgrado)
        )

    # 📅 FILTRO AÑO (FIX)
    if anio and anio.isdigit():
        materiales = materiales.filter(anio=int(anio))

    # 🔽 ORDENAMIENTO
    if orden == 'anio_desc':
        materiales = materiales.order_by('-anio')
    elif orden == 'anio_asc':
        materiales = materiales.order_by('anio')
    elif orden == 'autor':
        materiales = materiales.order_by('autor')
    elif orden == 'titulo':
        materiales = materiales.order_by('titulo')

    # 📄 PAGINACIÓN
    paginator = Paginator(materiales, 5)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    programas = Programa.objects.all()

    context = {
        'materiales': page_obj,
        'page_obj': page_obj,
        'programas': programas,
        'query': query,
        'selected_programa': programa_id,
        'selected_posgrado': posgrado,
        'selected_anio': anio,
        'orden': orden,
    }

    return render(request, 'core/buscador.html', context)


def home(request):
    materiales = Material.objects.order_by('-fecha_subida')[:6]
    return render(request, 'core/home.html', {'materiales': materiales})


def lista_carreras(request):
    carreras = Carrera.objects.all()
    return render(request, 'core/carreras.html', {'carreras': carreras})


def programas_por_carrera(request, carrera_id):
    programas = Programa.objects.filter(carrera_id=carrera_id)
    return render(request, 'core/programas.html', {'programas': programas})


def materiales_por_programa(request, programa_id):
    materiales = Material.objects.filter(programa_id=programa_id)
    return render(request, 'core/materiales.html', {'materiales': materiales})


def detalle_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)

    return render(request, 'core/detalle_material.html', {
        'material': material
    })
    
def programas(request, carrera_id):
    carrera = Carrera.objects.get(id=carrera_id)
    programas = Programa.objects.filter(carrera=carrera)

    return render(request, 'core/programas.html', {
        'carrera': carrera,
        'programas': programas
    })