from django.urls import URLPattern, path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cargarAlumnos', views.cargar_alumnos, name='cargar_alumnos'),
    path('listarAlumnos', views.listar_alumnos, name='listar_alumnos'),
    path('obtenerAlumno/<int:dni>', views.obtener_alumno, name='obtener_alumno'),
    path('alumno/', views.alumno, name='alumno'),
    path('alumno/<int:dni>/', views.alumno, name='alumno'),
    path('modificarAlumno', views.modificar_alumno, name='modificar_alumno'),
    path('modificarAlumno/<int:dni>', views.editar_alumno, name='editar_alumno'),
    path('eliminarAlumno/<int:dni>', views.eliminar_alumno, name='eliminar_alumno'),
    path('asignarCurso', views.asignar_curso, name='asignar_curso'),
    path('asignarCurso/<int:dni>/<int:id_curso>', views.asignar_curso, name='asignar_curso'),
    path('alumnosPorCurso', views.alumnos_por_curso, name='alumnos_por_curso'),
]
