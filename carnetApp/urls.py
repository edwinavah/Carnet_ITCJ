from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import dashboard, ActividadViewset, actividades, modificar_actividad, eliminar_actividad, ConferencistasViewset, conferencistas, modificar_conferencista, eliminar_conferencista, AlumnoViewset, alumnos, modificar_alumno, eliminar_alumno

router = routers.DefaultRouter()
router.register('actividades', ActividadViewset)
router.register('conferencistas', ConferencistasViewset)
router.register('alumnos', AlumnoViewset)

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('actividades/', actividades, name="actividades"),
    path('modificar-actividad/<id>/', modificar_actividad, name="modificar-actividad"),
    path('eliminar-actividad/<id>/', eliminar_actividad, name="eliminar-actividad"),
    path('conferencistas/', conferencistas, name="conferencistas"),
    path('modificar-conferencista/<id>/', modificar_conferencista, name="modificar-conferencista"),
    path('eliminar-conferencista/<id>/', eliminar_conferencista, name="eliminar-actividad"),
    path('alumnos/', alumnos, name="alumnos"),
    path('modificar-alumno/<id>/', modificar_alumno, name="modificar-alumno"),
    path('eliminar-alumno/<id>/', eliminar_alumno, name="eliminar-alumno"),
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)