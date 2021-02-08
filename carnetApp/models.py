from __future__ import unicode_literals
from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.
class Alumno(models.Model):
    CARRERA = (('Ingenieria en Sistemas Computacionales', 'Ingenieria en Sistemas Computacionales'),
            ('Ingenieria Industrial', 'Ingenieria Industrial'),
            ('Ingenieria en Gestion Empresarial', 'Ingenieria en Gestion Empresarial'),
            ('Licenciatura en Administracion', 'Licenciatura en Administracion'))

    no_control = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999)], null=False, verbose_name="Numero de control")
    nombre = models.CharField(max_length=250, null=False, verbose_name="Nombre(s)")
    apellidos = models.CharField(max_length=250, null=False)
    carrera = models.CharField(max_length=250, null=False, choices=CARRERA)
    correo = models.EmailField(max_length=250, null=False)

    def __str__(self):
        return str(self.no_control)

class Conferencista(models.Model):
    DEPARTAMENTO = (('Economico y Administrativo', 'Economico y Administrativo'),
            ('Ciencias Basicas', 'Ciencias Basicas'),
            ('Metal-Mecanica', 'Metal-Mecanica'),
            ('Electrica y Electronica', 'Electrica y Electronica'),
            ('Desarrollo Academico', 'Desarrollo Academico'),
            ('Sistemas y Computacion', 'Sistemas y Computacion'),
            ('Ingenieria Industrial', 'Ingenieria Industrial'),
            ('Division de Estudios Porfesionales', 'Division de Estudios Profesionales'),
            ('Posgrado e Investigacion', 'Posgrado e Investigacion'),
            ('Coordinacion de Educacion a Distancia', 'Coordinacion de Educacion a Distancia'),
            ('Planeacion, Programacion y Presupuestacion', 'Planeacion, Programacion y Presupuestacion'),
            ('Comunicacion y Difucion', 'Comunicacion y Difucion'),
            ('Servicios Escolares', 'Servicios Escolares'),
            ('Gestion Tecnologia y Vinculacion', 'Gestion Tecnologia y Vinculacion'),
            ('Actividades Extraescolares (Formacion Integral)', 'Actividades Extraescolares (Formacion Integral)'),
            ('Centro de Informacion (Biblioteca)', 'Centro de Informacion (Biblioteca)'))

    usuario = models.CharField(max_length=250, primary_key=True, null=False)
    nombre = models.CharField(max_length=250, null=False, verbose_name="Nombre(s)")
    apellidos = models.CharField(max_length=250, null=False)
    departamento = models.CharField(max_length=250, choices=DEPARTAMENTO)
    correo = models.EmailField(max_length=250, null=False)

    def __str__(self):
        return str(self.correo)

class Actividad(models.Model):
    DEPARTAMENTO = (('Economico y Administrativo', 'Economico y Administrativo'),
            ('Ciencias Basicas', 'Ciencias Basicas'),
            ('Metal-Mecanica', 'Metal-Mecanica'),
            ('Electrica y Electronica', 'Electrica y Electronica'),
            ('Desarrollo Academico', 'Desarrollo Academico'),
            ('Sistemas y Computacion', 'Sistemas y Computacion'),
            ('Ingenieria Industrial', 'Ingenieria Industrial'),
            ('Division de Estudios Porfesionales', 'Division de Estudios Profesionales'),
            ('Posgrado e Investigacion', 'Posgrado e Investigacion'),
            ('Coordinacion de Educacion a Distancia', 'Coordinacion de Educacion a Distancia'),
            ('Planeacion, Programacion y Presupuestacion', 'Planeacion, Programacion y Presupuestacion'),
            ('Comunicacion y Difucion', 'Comunicacion y Difucion'),
            ('Servicios Escolares', 'Servicios Escolares'),
            ('Gestion Tecnologia y Vinculacion', 'Gestion Tecnologia y Vinculacion'),
            ('Actividades Extraescolares (Formacion Integral)', 'Actividades Extraescolares (Formacion Integral)'),
            ('Centro de Informacion (Biblioteca)', 'Centro de Informacion (Biblioteca)'))

    codigo_qr = models.CharField(primary_key=True, max_length=500, null=False, verbose_name="Codigo QR")
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