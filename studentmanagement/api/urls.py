from django.urls import path , include
from rest_framework import routers
router = routers.DefaultRouter()
from .views import *
router.register(r'students', StudentViewset , basename='student')
router.register(r'courses', CourseViewset , basename='course')
router.register(r'results', ResultViewset , basename='result')

urlpatterns = [
    
    path('',include(router.urls)),
    path('students/results/<str:roll_number>/results', StudentResultViewset.as_view(), name='student-results'),
]
