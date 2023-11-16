# Generated by Django 4.2.6 on 2023-11-02 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BandaHoraria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Horario_inicio', models.DateTimeField()),
                ('Horaio_fin', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=250)),
                ('Nota', models.IntegerField()),
                ('BandaHoraria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.bandahoraria')),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('DNI', models.IntegerField(primary_key=True, serialize=False)),
                ('Telefono', models.IntegerField()),
                ('Correo_electronico', models.EmailField(max_length=254)),
                ('Curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.curso')),
            ],
        ),
    ]