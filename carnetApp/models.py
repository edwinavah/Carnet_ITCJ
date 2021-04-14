from __future__ import unicode_literals
from django.core.validators import MaxValueValidator
from django.db import models
import uuid
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
#
#
# class UsuarioManager(BaseUserManager):
#     def create_user(self, email, username, first_name, last_name, password=None):
#         if not email:
#             raise ValueError('El correo electronico es obligatorio')
#         user = self.model(username=username,
#                           email=self.normalize_email(email),
#                           first_name=first_name,
#                           last_name=last_name)
#
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, username, email, first_name, last_name, password):
#         user = self.create_user(email,
#                                 username=username,
#                                 first_name=first_name,
#                                 last_name=last_name,
#                                 password=password)
#         user.user_admin = True
#         user.save()
#         return user
#
#
# class Usuario(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=255, unique=True, verbose_name="Usuario")
#     email = models.EmailField(max_length=255, unique=True, verbose_name="Correo electronico")
#     first_name = models.CharField(max_length=255, blank=False, null=False, verbose_name="Nombre(s)")
#     last_name = models.CharField(max_length=255, blank=False, null=False, verbose_name="Apellidos")
#     user_active = models.BooleanField(default=True)
#     user_admin = models.BooleanField(default=False)
#     img = models.ImageField(upload_to="usuarios/", height_field=None, width_field=None, blank=True, null=True)
#     objects = UsuarioManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
#
#     def __str__(self):
#         return str(self.first_name)
#
#     def has_perm(self, perm, obj=None):
#         return True
#
#     def has_module_perms(self, app_label):
#         return True
#
#     @property
#     def is_staff(self):
#         return self.user_admin


# Create your models here.
class Alumno(models.Model):
    CARRERA = (('Licenciatura en Administracion', 'Licenciatura en Administracion'),
            ('Contador Publico', 'Contador Publico'),
            ('Ingenieria Mecanica', 'Ingenieria Mecanica'),
            ('Ingenieria en Sistemas Computacionales', 'Ingenieria en Sistemas Computacionales'),
            ('Ingenieria Electronica', 'Ingenieria Electronica'),
            ('Ingenieria en Tecnologias de la Informacion y Comunicaciones', 'Ingenieria en Tecnologias de la Informacion y Comunicaciones'),
            ('Ingenieria en Gestion Empresarial', 'Ingenieria en Gestion Empresarial'),
            ('Ingenieria Electrica', 'Ingenieria Electrica'),
            ('Ingenieria Industrial', 'Ingenieria Industrial'),
            ('Ingenieria en Logistica', 'Ingenieria en Logistica'),
            ('Ingenieria Mecatronica', 'Ingenieria Mecatronica'))

    no_control = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999)], null=False, verbose_name="Numero de control")
    nombre = models.CharField(max_length=250, null=False, verbose_name="Nombre(s)")
    apellidos = models.CharField(max_length=250, null=False)
    carrera = models.CharField(max_length=250, null=False, choices=CARRERA)
    correo = models.EmailField(max_length=250, null=False)
    password = models.CharField(max_length=250, null=False, verbose_name="Contraseña", default="Tecno#2K")

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
        ('Division de Estudios Profesionales', 'Division de Estudios Profesionales'),
        ('Posgrado e Investigacion', 'Posgrado e Investigacion'),
        ('Coordinacion de Educacion a Distancia', 'Coordinacion de Educacion a Distancia'),
        ('Planeacion, Programacion y Presupuestacion', 'Planeacion, Programacion y Presupuestacion'),
        ('Comunicacion y Difucion', 'Comunicacion y Difucion'),
        ('Servicios Escolares', 'Servicios Escolares'),
        ('Gestion Tecnologia y Vinculacion', 'Gestion Tecnologia y Vinculacion'),
        ('Actividades Extraescolares (Formacion Integral)', 'Actividades Extraescolares (Formacion Integral)'),
        ('Centro de Informacion (Biblioteca)', 'Centro de Informacion (Biblioteca)'),
        ('Otro/Externo', 'Otro/Externo'))

    correo = models.EmailField(max_length=250, null=False)
    nombre = models.CharField(max_length=250, null=False, verbose_name="Nombre(s)")
    apellidos = models.CharField(max_length=250, null=False)
    departamento = models.CharField(max_length=250, choices=DEPARTAMENTO)

    def __str__(self):
        return str(self.correo)

class Actividad(models.Model):
    codigo_qr = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=250, null=False)
    horas = models.IntegerField(null=False)
    fecha = models.DateTimeField(auto_now_add=True, null=False)
    impartidor = models.ForeignKey(Conferencista, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.codigo_qr)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.codigo_qr)
        canvas = Image.new('RGB', (380, 380), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'{self.codigo_qr}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.img.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True, null=False)