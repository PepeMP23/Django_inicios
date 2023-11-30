from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('students/', views.students, name='students'),
    path('students/details/<int:id>', views.details, name='details'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores, name='profesores'),
    path('materias/', views.materias, name='materias'),
    path('inscripciones/', views.inscripciones, name='inscripciones'),
    path('calificaciones/', views.calificaciones, name='calificaciones'),
    path('eventos/', views.eventos, name='eventos'),
    path('testing/', views.testing, name='testing'),  
]