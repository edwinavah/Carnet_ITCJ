from django.contrib import admin
from carnetApp.models import Alumno, Conferencista, Actividad, Asistencia
from django.contrib.auth.admin import UserAdmin

admin.site.site_header = 'Carnet TecNM'
admin.site.site_header = 'Carnet TecNM | Admin Dashboard'
admin.site.index_title = 'Administración de Carnet TecNM'

class AlumnoAdmin(admin.ModelAdmin):
    list_display=("no_control", "nombre", "apellidos", "carrera", "correo")

class ConferencistaAdmin(admin.ModelAdmin):
    list_display=("correo", "nombre", "apellidos", "departamento")

class ActividadAdmin(admin.ModelAdmin):
    list_display=("codigo_qr", "nombre", "horas", "fecha", "impartidor", "img")

class AsistenciaAdmin(admin.ModelAdmin):
    list_display=("alumno", "actividad", "fecha")

# class UsuarioAdmin(admin.ModelAdmin):
#     list_display=("username", "email", "first_name", "last_name", "is_active", "is_staff", "img")

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Conferencista, ConferencistaAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Asistencia, AsistenciaAdmin)
# admin.site.register(Usuario, UsuarioAdmin)