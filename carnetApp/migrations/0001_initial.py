# Generated by Django 3.1.5 on 2021-02-08 08:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('codigo_qr', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('horas', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('departamento', models.CharField(choices=[('Economico y Administrativo', 'Economico y Administrativo'), ('Ciencias Basicas', 'Ciencias Basicas'), ('Metal-Mecanica', 'Metal-Mecanica'), ('Electrica y Electronica', 'Electrica y Electronica'), ('Desarrollo Academico', 'Desarrollo Academico'), ('Sistemas y Computacion', 'Sistemas y Computacion'), ('Ingenieria Industrial', 'Ingenieria Industrial'), ('Division de Estudios Porfesionales', 'Division de Estudios Profesionales'), ('Posgrado e Investigacion', 'Posgrado e Investigacion'), ('Coordinacion de Educacion a Distancia', 'Coordinacion de Educacion a Distancia'), ('Planeacion, Programacion y Presupuestacion', 'Planeacion, Programacion y Presupuestacion'), ('Comunicacion y Difucion', 'Comunicacion y Difucion'), ('Servicios Escolares', 'Servicios Escolares'), ('Gestion Tecnologia y Vinculacion', 'Gestion Tecnologia y Vinculacion'), ('Actividades Extraescolares (Formacion Integral)', 'Actividades Extraescolares (Formacion Integral)'), ('Centro de Informacion (Biblioteca)', 'Centro de Informacion (Biblioteca)')], max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('no_control', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('nombre', models.CharField(max_length=250)),
                ('apellidos', models.CharField(max_length=250)),
                ('carrera', models.CharField(choices=[('Ingenieria en Sistemas Computacionales', 'Ingenieria en Sistemas Computacionales'), ('Ingenieria Industrial', 'Ingenieria Industrial'), ('Ingenieria en Gestion Empresarial', 'Ingenieria en Gestion Empresarial'), ('Licenciatura en Administracion', 'Licenciatura en Administracion')], max_length=250)),
                ('correo', models.EmailField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Conferencista',
            fields=[
                ('usuario', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('apellidos', models.CharField(max_length=250)),
                ('departamento', models.CharField(choices=[('Economico y Administrativo', 'Economico y Administrativo'), ('Ciencias Basicas', 'Ciencias Basicas'), ('Metal-Mecanica', 'Metal-Mecanica'), ('Electrica y Electronica', 'Electrica y Electronica'), ('Desarrollo Academico', 'Desarrollo Academico'), ('Sistemas y Computacion', 'Sistemas y Computacion'), ('Ingenieria Industrial', 'Ingenieria Industrial'), ('Division de Estudios Porfesionales', 'Division de Estudios Profesionales'), ('Posgrado e Investigacion', 'Posgrado e Investigacion'), ('Coordinacion de Educacion a Distancia', 'Coordinacion de Educacion a Distancia'), ('Planeacion, Programacion y Presupuestacion', 'Planeacion, Programacion y Presupuestacion'), ('Comunicacion y Difucion', 'Comunicacion y Difucion'), ('Servicios Escolares', 'Servicios Escolares'), ('Gestion Tecnologia y Vinculacion', 'Gestion Tecnologia y Vinculacion'), ('Actividades Extraescolares (Formacion Integral)', 'Actividades Extraescolares (Formacion Integral)'), ('Centro de Informacion (Biblioteca)', 'Centro de Informacion (Biblioteca)')], max_length=250)),
                ('correo', models.EmailField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carnetApp.actividad')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carnetApp.alumno')),
            ],
        ),
        migrations.AddField(
            model_name='actividad',
            name='impartidor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carnetApp.conferencista'),
        ),
    ]
