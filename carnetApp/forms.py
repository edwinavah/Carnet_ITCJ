from django import forms
from .models import Actividad

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        # fields = ["nombre", "horas", "impartidor"]
        fields = '__all__'
