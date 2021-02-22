from django.urls import path
from carnetApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name="login_urls"),
    path('dashboard', views.dashboard, name="dashboard_urls"),
    path('actividades', views.actividades, name="actividades_urls"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)