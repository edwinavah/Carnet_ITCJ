from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import viewsets
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from pathlib import Path
import os
from .models import Usuario, Actividad, Asistencia, Alumno, Conferencista, Carrera, Departamento
from .forms import UserForm, ActivityForm, ExhibitorForm, StudentForm, CareerForm, DepartmentForm
from .serializers import ActivitySerializer, AttendSerializer, StudentSerializer, ExhibitorSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ActivityViewset(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActivitySerializer

class ExhibitorViewset(viewsets.ModelViewSet):
    queryset = Conferencista.objects.all()
    serializer_class = ExhibitorSerializer

class StudentViewset(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = StudentSerializer

class AttendViewset(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AttendSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['alumno']

@login_required
def administrators(request):
    queryset = request.GET.get("buscar")
    administrators = Usuario.objects.all()
    if queryset:
        administrators = Usuario.objects.filter(
            Q(username__icontains=queryset)
        ).distinct()

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(administrators, 15)
        administrators = paginator.page(page)
    except:
        raise Http404

    data = {
        'administrators': administrators,
        'form': UserForm(),
        'paginator': paginator
    }

    # Agregar nueva actividad
    if request.method == 'POST':
        form = UserForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Se agrego correctamente")
            return redirect(to="administrators")
        else:
            data["form"] = form

    return render(request, "registration/administrators.html", data)

@login_required
def edit_administrators(request, id):
    administrators = get_object_or_404(Usuario, id=id)

    data = {
        'form': UserForm(instance=administrators)
    }

    if request.method == 'POST':
        form = UserForm(data=request.POST, instance=administrators, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Se modifico correctamente")
            return redirect(to="administrators")
        data["form"] = form

    return render(request, "registration/edit-administrators.html", data)

@login_required
def delete_administrators(request, id):
    administrators = get_object_or_404(Usuario, id=id)
    administrators.delete()
    messages.success(request, "Se eliminó correctamente")
    return redirect(to="administrators")

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

#Carrera
@login_required
def career(request):
    queryset = request.GET.get("buscar")
    career = Carrera.objects.all()
    if queryset:
        career = Carrera.objects.filter(
            Q(nombre__icontains=queryset)
        ).distinct()

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(career, 15)
        career = paginator.page(page)
    except:
        raise Http404

    data = {
        'career': career,
        'form': CareerForm(),
        'paginator': paginator
    }

    # Agregar nueva actividad
    if request.method == 'POST':
        form = CareerForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Se agrego correctamente")
            return redirect(to="career")
        else:
            data["form"] = form

    return render(request, "career/career.html", data)

@login_required
def edit_career(request, id):
    career = get_object_or_404(Carrera, id=id)

    data = {
        'form': CareerForm(instance=career)
    }

    if request.method == 'POST':
        form = CareerForm(data=request.POST, instance=career)
        if form.is_valid():
            form.save()
            messages.success(request, "Se modifico correctamente")
            return redirect(to="career")
        data["form"] = form

    return render(request, "career/edit-career.html", data)

@login_required
def delete_career(request, id):
    career = get_object_or_404(Carrera, id=id)
    career.delete()
    messages.success(request, "Se eliminó correctamente")
    return redirect(to="career")

#Departamentos del Instituto
@login_required
def department(request):
    queryset = request.GET.get("buscar")
    department = Departamento.objects.all()
    if queryset:
        department = Departamento.objects.filter(
            Q(nombre__icontains=queryset)
        ).distinct()

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(department, 15)
        department = paginator.page(page)
    except:
        raise Http404

    data = {
        'department': department,
        'form': CareerForm(),
        'paginator': paginator
    }

    # Agregar nueva actividad
    if request.method == 'POST':
        form = DepartmentForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Se agrego correctamente")
            return redirect(to="department")
        else:
            data["form"] = form

    return render(request, "department/department.html", data)

@login_required
def edit_department(request, id):
    department = get_object_or_404(Departamento, id=id)

    data = {
        'form': DepartmentForm(instance=department)
    }

    if request.method == 'POST':
        form = DepartmentForm(data=request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, "Se modifico correctamente")
            return redirect(to="department")
        data["form"] = form

    return render(request, "department/edit-department.html", data)

@login_required
def delete_department(request, id):
    department = get_object_or_404(Departamento, id=id)
    department.delete()
    messages.success(request, "Se eliminó correctamente")
    return redirect(to="department")

# Actividades
@login_required
def activity(request):
    queryset = request.GET.get("buscar")
    activity = Actividad.objects.all()
    if queryset:
        activity = Actividad.objects.filter(
            Q(nombre__icontains=queryset) |
            Q(impartidor__correo__icontains=queryset)
        ).distinct()

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(activity, 15)
        activity = paginator.page(page)
    except:
        raise Http404

    data = {
        'activity':activity,
        'form':ActivityForm(),
        'paginator':paginator
    }

    # Agregar nueva actividad
    if request.method == 'POST':
        form = ActivityForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Se agrego correctamente")
            return redirect(to="activity")
        else:
            data["form"] = form

    return render(request, "activity/activity.html", data)

@login_required
def edit_activity(request, id):
    activity = get_object_or_404(Actividad, codigo_qr=id)

    data = {
        'form':ActivityForm(instance=activity)
    }

    if request.method == 'POST':
        form = ActivityForm(data=request.POST, instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request, "Se modifico correctamente")
            return redirect(to="activity")
        data["form"] = form

    return render(request, "activity/edit-activity.html", data)

@login_required
def delete_activity(request, id):
    activity = get_object_or_404(Actividad, codigo_qr=id)
    activity.delete()

    BASE_DIR = Path(__file__).resolve().parent.parent
    MEDIA_ROOT = os.path.join(BASE_DIR, 'carnetApp/static/media')
    os.remove(os.path.join(MEDIA_ROOT+'/qr_codes/'+id+'.png'))

    messages.success(request, "Se eliminó correctamente")
    return redirect(to="activity")

# Activity Attend
@login_required
def activity_attend(request, id):
    attend = Asistencia.objects.filter(actividad=id)
    queryset = request.GET.get("buscar")
    if queryset:
        attend = Asistencia.objects.filter(
            Q(alumno__no_control__icontains=queryset, actividad=id)
        ).distinct()

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(attend, 15)
        attend = paginator.page(page)
    except:
        raise Http404

    data = {
        'attend':attend,
        'paginator':paginator
    }

    return render(request, "activity-attend/activity-attend.html", data)

# Exhibitor
@login_required
def exhibitor(request):
    queryset = request.GET.get("buscar")
    exhibitor = Conferencista.objects.all()
    if queryset:
        exhibitor = Conferencista.objects.filter(
            Q(nombre__icontains=queryset) |
            Q(apellidos__icontains=queryset) |
            Q(correo__icontains=queryset)
        ).distinct()

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(exhibitor, 15)
        exhibitor = paginator.page(page)
    except:
        raise Http404

    data = {
        'exhibitor': exhibitor,
        'form': ExhibitorForm(),
        'paginator': paginator
    }

    if request.method == 'POST':
        form = ExhibitorForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Se agrego correctamente")
            return redirect(to="exhibitor")
        else:
            data["form"] = form

    return render(request, "exhibitor/exhibitor.html", data)

@login_required
def edit_exhibitor(request, id):
    exhibitor = get_object_or_404(Conferencista, id=id)

    data = {
        'form':ExhibitorForm(instance=exhibitor)
    }

    if request.method == 'POST':
        form = ExhibitorForm(data=request.POST, instance=exhibitor)
        if form.is_valid():
            form.save()
            messages.success(request, "Se modifico correctamente")
            return redirect(to="exhibitor")
        data["form"] = form

    return render(request, "exhibitor/edit-exhibitor.html", data)

@login_required
def delete_exhibitor(request, id):
    exhibitor = get_object_or_404(Conferencista, id=id)
    exhibitor.delete()
    messages.success(request, "Se eliminó correctamente")
    return redirect(to="exhibitor")

# Students
@login_required
def student(request):
    queryset = request.GET.get("buscar")
    student = Alumno.objects.all()
    if queryset:
        student = Alumno.objects.filter(
            Q(no_control__icontains=queryset)
        ).distinct()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(student, 15)
        student = paginator.page(page)
    except:
        raise Http404

    data = {
        'student': student,
        'form': StudentForm(),
        'paginator': paginator
    }

    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Se agrego correctamente")
            return redirect(to="student")
        else:
            data["form"] = form

    return render(request, "student/student.html", data)

@login_required
def edit_student(request, id):
    student = get_object_or_404(Alumno, no_control=id)

    data = {
        'form':StudentForm(instance=student)
    }

    if request.method == 'POST':
        form = StudentForm(data=request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Se modifico correctamente")
            return redirect(to="student")
        data["form"] = form

    return render(request, "student/edit-student.html", data)

@login_required
def delete_student(request, id):
    student = get_object_or_404(Alumno, no_control=id)
    student.delete()
    messages.success(request, "Se eliminó correctamente")
    return redirect(to="student")

# Student Attend
@login_required
def student_attend(request, id):
    attend = Asistencia.objects.filter(alumno=id)
    sum_hours = Asistencia.objects.filter(alumno=id).aggregate(Sum('actividad__horas'))

    queryset = request.GET.get("buscar")
    if queryset:
        attend = Asistencia.objects.filter(
            Q(actividad__nombre__icontains=queryset, alumno=id)
        ).distinct()

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(attend, 15)
        attend = paginator.page(page)
    except:
        raise Http404

    data = {
        'attend': attend,
        'sum_hours':sum_hours,
        'paginator':paginator
    }

    return render(request, "activity-attend/student-attend.html", data)

