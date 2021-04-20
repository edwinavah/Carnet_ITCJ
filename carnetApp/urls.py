from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import dashboard, ActivityViewset, activity, edit_activity, delete_activity, \
    ExhibitorViewset, exhibitor, edit_exhibitor, delete_exhibitor, \
    StudentViewset, student, edit_student, delete_student, \
    AttendViewset, activity_attend, student_attend

router = routers.DefaultRouter()
router.register('activity', ActivityViewset)
router.register('exhibitor', ExhibitorViewset)
router.register('student', StudentViewset)
router.register('attend', AttendViewset)

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('activity/', activity, name="activity"),
    path('edit-activity/<id>/', edit_activity, name="edit-activity"),
    path('delete-activity/<id>/', delete_activity, name="delete-activity"),
    path('activity-attend/<id>/', activity_attend, name="activity-attend"),
    path('exhibitor/', exhibitor, name="exhibitor"),
    path('edit-exhibitor/<id>/', edit_exhibitor, name="edit-exhibitor"),
    path('delete-exhibitor/<id>/', delete_exhibitor, name="delete-exhibitor"),
    path('student/', student, name="student"),
    path('edit-student/<id>/', edit_student, name="edit-student"),
    path('delete-student/<id>/', delete_student, name="delete-student"),
    path('student-attend/<id>/', student_attend, name="student-attend"),
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)