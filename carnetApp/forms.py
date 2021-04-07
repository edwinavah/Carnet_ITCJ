from django import forms
from .models import Actividad, Conferencista, Alumno

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ["nombre", "horas", "impartidor"]

class ConferencistaForm(forms.ModelForm):
    class Meta:
        model = Conferencista
        fields = ["nombre", "apellidos", "correo", "departamento"]

class AlumnoForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Alumno
        fields = ["no_control", "nombre", "apellidos", "carrera", "correo"]