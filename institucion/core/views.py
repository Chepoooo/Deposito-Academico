from django.shortcuts import render
from django.db.models import Q
from academico.models import Carrera, Programa
from materiales.models import Material

def buscador(request):
    query = request.GET.get('q', '')
    carrera_id = request.GET.get('carrera')
    programa_id = request.GET.get('programa')
    anio = request.GET.get('anio')

    materiales = Material.objects.all()

    if query:
        materiales = materiales.filter(
            Q(titulo__icontains=query) |
            Q(autor__icontains=query)
        )

    if carrera_id:
        materiales = materiales.filter(programa__carrera_id=carrera_id)

    if programa_id:
        materiales = materiales.filter(programa_id=programa_id)

    if anio:
        materiales = materiales.filter(anio=anio)

    context = {
        'materiales': materiales,
        'carreras': Carrera.objects.all(),
        'programas': Programa.objects.all(),
        'query': query,
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
