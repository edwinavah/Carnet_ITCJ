from __future__ import unicode_literals
from django.core.validators import MaxValueValidator
from django.db import models
import uuid

# Create your models here.
class Alumno(models.Model):
    CARRERA = (('ing-sistemas-computacionales', 'Ingenieria en Sistemas Computacionales'),
            ('ing-industrial', 'Ingenieria Industrial'),
            ('ing-gestion-empresarial', 'Ingenieria en Gestion Empresarial'),
            ('lic-administracion', 'Licenciatura en Administracion'))

    no_control = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999)], null=False, verbose_name="Numero de control")
    nombre = models.CharField(max_length=250, null=False, verbose_name="Nombre(s)")
    apellidos = models.CharField(max_length=250, null=False)
    carrera = models.CharField(max_length=250, null=False, choices=CARRERA)
    correo = models.EmailField(max_length=250, null=False)

    def __str__(self):
        return str(self.no_control)

class Conferencista(models.Model):
    DEPARTAMENTO = (('economico-administrativo', 'Economico y Administrativo'),
        ('ciencias-basicas', 'Ciencias Basicas'),
        ('metal-mecanica', 'Metal-Mecanica'),
        ('electrica-electronica', 'Electrica y Electronica'),
        ('desarrollo-academico', 'Desarrollo Academico'),
        ('sistemas-computacion', 'Sistemas y Computacion'),
        ('ingenieria-industrial', 'Ingenieria Industrial'),
        ('division-estudios-Profesionales', 'Division de Estudios Profesionales'),
        ('posgrado-investigacion', 'Posgrado e Investigacion'),
        ('coordinacion-educacion-distancia', 'Coordinacion de Educacion a Distancia'),
        ('planeacion-programacion-presupuestacion', 'Planeacion, Programacion y Presupuestacion'),
        ('comunicacion-difucion', 'Comunicacion y Difucion'),
        ('servicios-escolares', 'Servicios Escolares'),
        ('gestion-tecnologia-vinculacion', 'Gestion Tecnologia y Vinculacion'),
        ('actividades-extraescolares', 'Actividades Extraescolares (Formacion Integral)'),
        ('centro-informacion', 'Centro de Informacion (Biblioteca)'))

    correo = models.EmailField(max_length=250, primary_key=True, null=False)
    nombre = models.CharField(max_length=250, null=False, verbose_name="Nombre(s)")
    apellidos = models.CharField(max_length=250, null=False)
    departamento = models.CharField(max_length=250, choices=DEPARTAMENTO)

    def __str__(self):
        return str(self.correo)

class Actividad(models.Model):
    DEPARTAMENTO = (('economico-administrativo', 'Economico y Administrativo'),
        ('ciencias-basicas', 'Ciencias Basicas'),
        ('metal-mecanica', 'Metal-Mecanica'),
        ('electrica-electronica', 'Electrica y Electronica'),
        ('desarrollo-academico', 'Desarrollo Academico'),
        ('sistemas-computacion', 'Sistemas y Computacion'),
        ('ingenieria-industrial', 'Ingenieria Industrial'),
        ('division-estudios-Profesionales', 'Division de Estudios Profesionales'),
        ('posgrado-investigacion', 'Posgrado e Investigacion'),
        ('coordinacion-educacion-distancia', 'Coordinacion de Educacion a Distancia'),
        ('planeacion-programacion-presupuestacion', 'Planeacion, Programacion y Presupuestacion'),
        ('comunicacion-difucion', 'Comunicacion y Difucion'),
        ('servicios-escolares', 'Servicios Escolares'),
        ('gestion-tecnologia-vinculacion', 'Gestion Tecnologia y Vinculacion'),
        ('actividades-extraescolares', 'Actividades Extraescolares (Formacion Integral)'),
        ('centro-informacion', 'Centro de Informacion (Biblioteca)'))

    codigo_qr = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=250, null=False)
    horas = models.IntegerField(null=False)
    fecha = models.DateTimeField(auto_now_add=True, null=False)
    impartidor = models.ForeignKey(Conferencista, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)

class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True, null=False)