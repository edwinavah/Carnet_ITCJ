from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from .models import Actividad, Asistencia, Alumno, Conferencista
from .forms import ActividadForm
from rest_framework import viewsets
from .serializers import ActividadSerializer, AsistenciaSerializer, AlumnoSerializer, ConferencistaSerializer
from django.core.paginator import Paginator
from django.http import Http404

class ActividadViewset(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

def login(request):
    return render(request, "login.html")

def dashboard(request):
    return render(request, "dashboard.html")

def actividades(request):
    actividad = Actividad.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(actividad, 15)
        actividad = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'actividad':actividad,
        'form':ActividadForm(),
        'paginator':paginator
    }

    if request.method == 'POST':
        formulario = ActividadForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se agrego correctamente")
        else:
            data["form"] = formulario

    return render(request, "actividades/actividades.html", data)

def modificar_actividad(request, id):
    actividad = get_object_or_404(Actividad, codigo_qr=id)

    data = {
        'form':ActividadForm(instance=actividad)
    }

    if request.method == 'POST':
        formulario = ActividadForm(data=request.POST, instance=actividad)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se modifico correctamente")
            return redirect(to="actividades")
        data["form"] = formulario

    return render(request, "actividades/modificar-actividad.html", data)

def eliminar_actividad(request, id):
    actividad = get_object_or_404(Actividad, codigo_qr=id)
    actividad.delete()
    messages.success(request, "Se eliminó correctamente")
    return redirect(to="actividades")