from django import forms
from .models import Usuario, Actividad, Conferencista, Alumno, Carrera, Departamento

class UserForm(forms.ModelForm):
    # password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Ingrese la contraseña',
    #         'id': 'password1',
    #         'required': 'required',
    #     }
    # ))
    #
    # password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Ingrese nuevamente la contraseña',
    #         'id': 'password2',
    #         'required': 'required',
    #     }
    # ))

    class Meta:
        model = Usuario
        fields = ["username", "first_name", "last_name", "user_active", "user_admin", "password", "img"]

class CareerForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ["nombre"]

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ["nombre"]

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ["nombre", "horas", "impartidor"]

class ExhibitorForm(forms.ModelForm):
    class Meta:
        model = Conferencista
        fields = ["nombre", "apellidos", "correo", "departamento"]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ["no_control", "nombre", "apellidos", "carrera", "correo"]
