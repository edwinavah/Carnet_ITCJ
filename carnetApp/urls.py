from django.urls import path, include
from carnetApp import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import login, dashboard, actividades, modificar_actividad, ActividadViewset, eliminar_actividad

router = routers.DefaultRouter()
router.register('actividades', ActividadViewset)

urlpatterns = [
    path('', login, name="login"),
    path('dashboard/', dashboard, name="dashboard"),
    path('actividades/', actividades, name="actividades"),
    path('modificar-actividad/<id>/', modificar_actividad, name="modificar-actividad"),
    path('eliminar-actividad/<id>/', eliminar_actividad, name="eliminar-actividad"),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)