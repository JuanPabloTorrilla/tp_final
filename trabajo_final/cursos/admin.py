from django.contrib import admin
from .models import BandaHoraria, Curso, Alumno

# Register your models here.
class BandaHorariaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["Nombre", "Horario_inicio", "Horario_fin"]})
    ]

class CursoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["Nombre", "Descripcion", "BandaHoraria", "Nota"]})
    ]
    
class AlumnoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["Nombre", "Apellido", "DNI", "Telefono", "Correo_electronico", "Curso"]})
    ]
    
admin.site.register(BandaHoraria, BandaHorariaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Alumno, AlumnoAdmin)