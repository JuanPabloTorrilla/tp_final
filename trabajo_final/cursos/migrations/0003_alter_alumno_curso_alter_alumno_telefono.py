# Generated by Django 4.2.6 on 2023-11-06 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_rename_horaio_fin_bandahoraria_horario_fin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='Curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cursos.curso'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='Telefono',
            field=models.CharField(max_length=15),
        ),
    ]
