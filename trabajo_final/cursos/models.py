from django.db import models

# Create your models here.
class BandaHoraria(models.Model):
    Nombre = models.CharField(max_length=50)
    Horario_inicio = models.DateTimeField()
    Horario_fin = models.DateTimeField()
    
class Curso(models.Model):
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=250)
    BandaHoraria = models.ForeignKey(BandaHoraria, on_delete=models.CASCADE)
    Nota = models.IntegerField()    
    
class Alumno(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    DNI = models.IntegerField(primary_key=True)
    Telefono = models.CharField(max_length=15)
    Correo_electronico = models.EmailField()
    Curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    

    
