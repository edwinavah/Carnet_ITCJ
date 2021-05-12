from django import forms
from .models import Usuario, Actividad, Conferencista, Alumno, Carrera, Departamento

class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["username", "first_name", "last_name", "user_active", "user_admin", "email", "password", "img"]
        widgets = {
            'password':forms.PasswordInput(
                attrs = {
                    'value': 'Tecno#2K#Admin',
                    'type': 'hidden',
                }
            )
        }
    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

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
