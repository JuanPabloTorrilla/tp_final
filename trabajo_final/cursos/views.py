from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.core import serializers
import json
from .models import Alumno, Curso, BandaHoraria
import csv

def index(request):
    template = loader.get_template('cursos/index.html')
    cursos = get_list_or_404(Curso)
    context = {
        'cursos': cursos
    }
    return HttpResponse(template.render(context, request))

def cargar_alumnos(request):
    if request.method == "POST":
        fileReader = request.FILES['file'].read().decode("utf-8")
        lines = fileReader.split('\n')
        for line in lines:
            alumnos = line.split(',')
            if alumnos[2].isdigit() == False:
                print(type(alumnos[2]))
                continue
            else: 
                if Alumno.objects.filter(DNI__contains=alumnos[2]):
                    continue
                qCurso = None
                try:
                    qCurso = Curso.objects.get(Nombre=alumnos[5])
                except:
                    qCurso = None

                Alumno.objects.create(
                Nombre = alumnos[0],
                Apellido = alumnos[1],
                DNI = alumnos[2],
                Telefono = alumnos[3],
                Correo_electronico = alumnos[4],
                Curso = qCurso,
                )
        return HttpResponseRedirect("/cursos/listarAlumnos")
    if request.method == "GET":
        template = loader.get_template('cursos/cargarAlumno.html')
        context = {}
        return HttpResponse(template.render(context, request))
        

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    template = loader.get_template("cursos/listarAlumnos.html")
    context = {
        "alumnos": alumnos,
    }
    return HttpResponse(template.render(context, request))

def obtener_alumno(request, dni):
    alumno = get_object_or_404(Alumno, DNI=dni)
    template = loader.get_template("cursos/detail.html")
    context = {
        "alumno": alumno,
    }
    return HttpResponse(template.render(context, request))

def alumno(request):
    dni = request.GET.get('dni')
    alumno = get_object_or_404(Alumno, DNI=dni)
    try:
        curso = get_object_or_404(Curso, id = alumno.Curso.id) 
        bandaHoraria = get_object_or_404(BandaHoraria, id=curso.BandaHoraria.id)
        model_fields = alumno._meta.fields + alumno._meta.many_to_many + curso._meta.fields + curso._meta.many_to_many + bandaHoraria._meta.fields + bandaHoraria._meta.many_to_many
        field_names = [field.name for field in model_fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="alumno %s.csv"'%(alumno.DNI)
        # the csv writer
        writer = csv.writer(response, delimiter=",")
        # Write a first row with header information
        writer.writerow(field_names)
        values = [alumno.Nombre,alumno.Apellido,alumno.DNI,alumno.Telefono,alumno.Correo_electronico,alumno.Curso,alumno.Curso.id,alumno.Curso.Nombre,alumno.Curso.Descripcion,alumno.Curso.BandaHoraria,alumno.Curso.Nota,alumno.Curso.BandaHoraria.id,alumno.Curso.BandaHoraria.Nombre,alumno.Curso.BandaHoraria.Horario_inicio,alumno.Curso.BandaHoraria.Horario_fin]
        print(values)
        writer.writerow(values)

        return response  
    except Exception as e:
        print(e)
        return HttpResponse('Al alumno no se le ha asignado curso aún. Error:%s'%(e))
    
def editar_alumno(request, dni):
    alumno = get_object_or_404(Alumno, DNI=dni)
    if request.method == 'GET':
        template = loader.get_template("cursos/editAlumno.html")
        context = {
            "alumno": alumno,
        }
        return HttpResponse(template.render(context, request))
    if request.method == 'POST':
        alumno.Nombre = request.POST['nombre']
        alumno.Apellido = request.POST['apellido']
        alumno.DNI = request.POST['dni']
        alumno.Telefono = request.POST['telefono']
        alumno.Correo_electronico = request.POST['correo_electronico']
        alumno.save()
        return redirect(obtener_alumno, dni)
    
def modificar_alumno(request):
    if request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        dni = data['dni']
        alumno = get_object_or_404(Alumno, DNI=dni)
        alumno.Nombre = data['nombre']
        alumno.Apellido = data['apellido']
        alumno.DNI = data['dni']
        alumno.Telefono = data['telefono']
        alumno.Correo_electronico = data['correo_electronico']
        alumno.save()
        return redirect(obtener_alumno, dni)
    
def eliminar_alumno(request, dni):
    if request.method == 'GET':
        alumno = get_object_or_404(Alumno, DNI=dni)
        alumno.delete()
        return redirect(listar_alumnos)
    if request.method == 'DELETE':
        try:
            alumno = get_object_or_404(Alumno, DNI=dni)
            alumno.delete()
            return HttpResponse('Los datos del alumno han sido eliminados')
        except Exception as e:
            return HttpResponse('No existe registro del alumno. Error: %s'%(e))

def asignar_curso(request):
    dni = request.POST.get('dni')
    id = request.POST.get('id')
    print(dni,id)
    if request.method == 'GET':
        template = loader.get_template("cursos/asignarCurso.html")
        context = {
            "alumnos": Alumno.objects.all(),
            "cursos": Curso.objects.all(),
        }
        return HttpResponse(template.render(context, request))
    if request.method == 'POST':
        alumno = get_object_or_404(Alumno, DNI=dni)
        curso = get_object_or_404(Curso, id=id)
        alumno.Curso = curso
        alumno.save()
        return HttpResponse("Al alumno %s %s, dni %s, se le ha asignado el curso %s"%(alumno.Nombre, alumno.Apellido, alumno.DNI, curso.Nombre))

def alumnos_por_curso(request):
    id = request.GET.get('id')
    curso = get_object_or_404(Curso,id=id)
    alumnos = Alumno.objects.filter(Curso=curso)
    serialized_alumnos = json.dumps([{'nombre':alumno.Nombre,'apellido':alumno.Apellido,'dni':alumno.DNI,'telefono':alumno.Telefono,'correo_electronico':alumno.Correo_electronico}for alumno in alumnos], ensure_ascii=False)
    print(serialized_alumnos)
    return HttpResponse(serialized_alumnos, content_type="application/json")