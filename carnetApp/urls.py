from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import dashboard, ActivityViewset, activity, edit_activity, delete_activity, \
    ExhibitorViewset, exhibitor, edit_exhibitor, delete_exhibitor, \
    StudentViewset, student, edit_student, delete_student, \
    AttendViewset, activity_attend, student_attend, \
    career, edit_career, delete_career, \
    department, edit_department, delete_department, \
    administrators, edit_administrators, delete_administrators, \
    CareerViewset, DepartamentViewset

router = routers.DefaultRouter()
router.register('activity', ActivityViewset)
router.register('exhibitor', ExhibitorViewset)
router.register('student', StudentViewset)
router.register('attend', AttendViewset)
router.register('career', CareerViewset)
router.register('departament', DepartamentViewset)

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('career/', career, name="career"),
    path('edit-career/<id>/', edit_career, name="edit-career"),
    path('delete-career/<id>/', delete_career, name="delete-career"),
    path('department/', department, name="department"),
    path('edit-department/<id>/', edit_department, name="edit-department"),
    path('delete-department/<id>/', delete_department, name="delete-department"),
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
    path('administrators/', administrators, name="administrators"),
    path('edit-administrators/<id>/', edit_administrators, name="edit-administrators"),
    path('delete-administrators/<id>/', delete_administrators, name="delete-administrators"),
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)