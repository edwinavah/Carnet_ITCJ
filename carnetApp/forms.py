from django import forms
from .models import Actividad, Conferencista, Alumno

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ["nombre", "horas", "impartidor"]

class ExhibitorForm(forms.ModelForm):
    class Meta:
        model = Conferencista
        fields = ["nombre", "apellidos", "correo", "departamento"]

class StudentForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Alumno
        fields = ["no_control", "nombre", "apellidos", "carrera", "correo"]