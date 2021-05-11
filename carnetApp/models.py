from __future__ import unicode_literals
from django.core.validators import MaxValueValidator
from django.db import models
import uuid
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError('El correo electronico es obligatorio')
        user = self.model(username=username,
                          email=self.normalize_email(email),
                          first_name=first_name,
                          last_name=last_name)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, first_name, last_name, password):
        user = self.create_user(email,
                                username=username,
                                first_name=first_name,
                                last_name=last_name,
                                password=password)
        user.user_admin = True
        user.save()
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, verbose_name="Usuario")
    email = models.EmailField(max_length=255, unique=True, verbose_name="Correo electronico")
    first_name = models.CharField(max_length=255, blank=False, null=False, verbose_name="Nombre(s)")
    last_name = models.CharField(max_length=255, blank=False, null=False, verbose_name="Apellidos")
    img = models.ImageField(upload_to="usuarios/", blank=True, null=True, verbose_name="Foto de perfil")
    user_active = models.BooleanField(default=True)
    user_admin = models.BooleanField(default=False)

    objects = UsuarioManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return str(self.first_name)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.user_admin

class Departamento(models.Model):
    nombre = models.CharField(max_length=250, null=False, unique=True)

    def __str__(self):
        return str(self.nombre)

class Carrera(models.Model):
    nombre = models.CharField(max_length=250, null=False, unique=True)

    def __str__(self):
        return str(self.nombre)

class Alumno(models.Model):
    no_control = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999)], null=False, verbose_name="Numero de control")
    nombre = models.CharField(max_length=250, null=False, verbose_name="Nombre(s)")
    apellidos = models.CharField(max_length=250, null=False)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    correo = models.EmailField(max_length=250, null=False, unique=True)
    password = models.CharField(max_length=250, null=False, verbose_name="Contraseña", default="Tecno#2K")

    def __str__(self):
        return str(self.no_control)

class Conferencista(models.Model):
    correo = models.EmailField(max_length=250, null=False, unique=True)
    nombre = models.CharField(max_length=250, null=False, verbose_name="Nombre(s)")
    apellidos = models.CharField(max_length=250, null=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

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
