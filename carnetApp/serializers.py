from .models import Actividad, Asistencia, Alumno, Conferencista
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
    impartidor = serializers.StringRelatedField()
    class Meta:
        model = Actividad
        fields = "__all__"

class AttendSerializer(serializers.ModelSerializer):
    actividad = serializers.StringRelatedField()
    class Meta:
        model = Asistencia
        fields = "__all__"