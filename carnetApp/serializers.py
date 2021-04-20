from .models import Actividad, Asistencia, Alumno, Conferencista
from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = "__all__"

class AttendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"


class ExhibitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conferencista
        fields = "__all__"