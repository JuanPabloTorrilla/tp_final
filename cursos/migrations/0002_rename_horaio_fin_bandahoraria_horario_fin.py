# Generated by Django 4.2.6 on 2023-11-03 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bandahoraria',
            old_name='Horaio_fin',
            new_name='Horario_fin',
        ),
    ]
