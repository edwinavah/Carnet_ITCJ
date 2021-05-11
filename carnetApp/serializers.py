from .models import Actividad, Asistencia, Alumno, Conferencista, Carrera, Departamento
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"

class ExhibitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conferencista
        fields = "__all__"

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = "__all__"

class AttendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = "__all__"

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = "__all__"

class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = "__all__"
