from django.shortcuts import render, redirect
from .models import UnidadAcademica, ProgramaAcademico
from .forms import FormUnidadAcademica, FormProgramaAcademico, FormFiltrosPrograma
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.
def bienvenida(request):
    return render(request, 'bienvenida.html')

def editar_unidad(request, id):
    unidad = UnidadAcademica.objects.get(id = id)
    if request.method == 'POST':
        form = FormUnidadAcademica(request.POST, instance=unidad)
        if form.is_valid():
            form.save()
            return redirect('lista_unidades')
    else:
        form = FormUnidadAcademica(instance=unidad)
    context = {'form': form}

    return render(request, 'editar_unidad.html', context)



def editar_programa(request, id):
    programa = ProgramaAcademico.objects.get(id = id)
    if request.method == 'POST':
        form = FormProgramaAcademico(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            return redirect('lista_programas')
    else:
        form = FormProgramaAcademico(instance=programa)
    context = {'form': form}

    return render(request, 'editar_programa.html', context)



def nueva_unidad(request):
    if request.method == 'POST':
        form = FormUnidadAcademica(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_unidades')
    else:
        form = FormUnidadAcademica()

    context = {'form': form}
    return render(request, 'nueva_unidad.html', context)

def nueva_unidad_ajax(request):
    if request.method == 'POST':
        form = FormUnidadAcademica(request.POST)
        if form.is_valid():
            unidad = form.save()
            unidades = list(UnidadAcademica.objects.all().values())
            response = {
                'ok': 'Se guardo la unidad con exito',
                'unidades': unidades,
                'unidad': unidad.id
            }
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse({'error': f'Error de validacion: {form.errors}'}, safe=False)
    else:
        return JsonResponse({'error': 'Metodo no permitido'}, safe=False)

def nuevo_programa(request):
    form_unidad = FormUnidadAcademica()
    if request.method == 'POST':
        form = FormProgramaAcademico(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_programas')
    else:
        form = FormProgramaAcademico()

    context = {'form': form, 'form_unidad': form_unidad}
    return render(request, 'nuevo_programa.html', context)


def lista_unidades_academicas(request):
    context = {'unidades' : UnidadAcademica.objects.all()}
    return render(request, 'lista_unidades.html', context)


def lista_programas_academicas(request):
    algo = ProgramaAcademico.objects.all()
    #programas = ProgramaAcademico.objects.all().get(id=21)
    # programas = ProgramaAcademico.objects.filter(nombre__startswith='Ingenieria')
    # programas = ProgramaAcademico.objects.filter(nombre__endswith='ware')
    # programas = ProgramaAcademico.objects.filter(nombre__contains='i')
    #programas = ProgramaAcademico.objects.exclude(nombre__startswith='I')[2:4]
    # print(programas.query)
    # context = {'programas' : ProgramaAcademico.objects.all()}
    
    
    if request.method == 'POST':
        form= FormFiltrosPrograma(request.POST)
        nombre = request.POST.get('nombre',None)
        descripcion = request.POST.get('descripcion',None)
        unidad = request.POST.get('unidad',None)
        cantidad_seleccionada = int(request.POST.get('cuantos', 10))
        if nombre:
            algo = algo.filter(nombre__icontains=nombre)
        if descripcion:
            algo = algo.filter(descripcion__icontains=descripcion)
        if unidad:
            algo = algo.filter(unidad_academica__nombre__icontains=unidad)
        
    else:
        form = FormFiltrosPrograma()
        cantidad_seleccionada = 10
    paginator = Paginator(algo, cantidad_seleccionada)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    programas = paginator.get_page(page_number)
    context = {'programas' :programas,'form':form,'cuantos':cantidad_seleccionada}
    return render(request,'lista_programas.html',context)

def eliminar_unidad(request, id):
    unidad = UnidadAcademica.objects.get(id=id)
    programas = ProgramaAcademico.objects.filter(unidad_academica = unidad)
    for programa in programas:
        programa.delete()

    unidad.delete()
    return redirect("lista_unidades")

def eliminar_programa(request, id):
    programa = ProgramaAcademico.objects.get(id=id)
    programa.delete()
    return redirect("lista_programas")