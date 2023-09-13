from django.urls import path
from . import views

urlpatterns = [
    path('Alumnos/', views.Alumnos, name='Alumnos'),
]