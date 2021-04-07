from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import viewsets
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required
from pathlib import Path
import os
from .models import Actividad, Asistencia, Alumno, Conferencista
from .forms import ActividadForm, ConferencistaForm, AlumnoForm
from .serializers import ActividadSerializer, AsistenciaSerializer, AlumnoSerializer, ConferencistaSerializer

class ActividadViewset(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class ConferencistasViewset(viewsets.ModelViewSet):
    queryset = Conferencista.objects.all()
    serializer_class = ConferencistaSerializer

class AlumnoViewset(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

# Actividades
@login_required
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
            return redirect(to="actividades")
        else:
            data["form"] = formulario

    return render(request, "actividades/actividades.html", data)

@login_required
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

@login_required
def eliminar_actividad(request, id):
    actividad = get_object_or_404(Actividad, codigo_qr=id)
    actividad.delete()

    BASE_DIR = Path(__file__).resolve().parent.parent
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    os.remove(os.path.join(MEDIA_ROOT+'/qr_codes/'+id+'.png'))

    messages.success(request, "Se eliminó correctamente")
    return redirect(to="actividades")

# Conferencistas
@login_required
def conferencistas(request):
    conferencista = Conferencista.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(conferencista, 15)
        conferencista = paginator.page(page)
    except:
        raise Http404

    data = {
        'conferencista': conferencista,
        'form': ConferencistaForm(),
        'paginator': paginator
    }

    if request.method == 'POST':
        formulario = ConferencistaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se agrego correctamente")
            return redirect(to="conferencistas")
        else:
            data["form"] = formulario

    return render(request, "conferencistas/conferencistas.html", data)

@login_required
def modificar_conferencista(request, id):
    conferencista = get_object_or_404(Conferencista, id=id)

    data = {
        'form':ConferencistaForm(instance=conferencista)
    }

    if request.method == 'POST':
        formulario = ConferencistaForm(data=request.POST, instance=conferencista)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se modifico correctamente")
            return redirect(to="conferencistas")
        data["form"] = formulario

    return render(request, "conferencistas/modificar-conferencista.html", data)

@login_required
def eliminar_conferencista(request, id):
    conferencista = get_object_or_404(Conferencista, id=id)
    conferencista.delete()
    messages.success(request, "Se eliminó correctamente")
    return redirect(to="conferencistas")

# Alumnos
@login_required
def alumnos(request):
    alumno = Alumno.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(alumno, 15)
        alumno = paginator.page(page)
    except:
        raise Http404

    data = {
        'alumno': alumno,
        'form': AlumnoForm(),
        'paginator': paginator
    }

    if request.method == 'POST':
        formulario = AlumnoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se agrego correctamente")
            return redirect(to="alumnos")
        else:
            data["form"] = formulario

    return render(request, "alumnos/alumnos.html", data)

@login_required
def modificar_alumno(request, id):
    alumno = get_object_or_404(Alumno, no_control=id)

    data = {
        'form':AlumnoForm(instance=alumno)
    }

    if request.method == 'POST':
        formulario = AlumnoForm(data=request.POST, instance=alumno)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se modifico correctamente")
            return redirect(to="alumnos")
        data["form"] = formulario

    return render(request, "alumnos/modificar-alumno.html", data)

@login_required
def eliminar_alumno(request, id):
    alumno = get_object_or_404(Alumno, no_control=id)
    alumno.delete()
    messages.success(request, "Se eliminó correctamente")
    return redirect(to="alumnos")
