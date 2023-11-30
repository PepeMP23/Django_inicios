from django.contrib import admin
from .models import Student, Estudiante, Profesores, Materias, Inscripciones, Calificaciones, Eventos

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
admin.site.register(Student, MemberAdmin)

class EstudianteAdmin(admin.ModelAdmin):
  list_display = ("idEstudiante", "nombre", "apellidoPaterno", "apellidoMaterno",)
admin.site.register(Estudiante, EstudianteAdmin)

class ProfesorAdmin(admin.ModelAdmin):
  list_display = ("idProfesor", "nombre", "apellidoPaterno", "apellidoMaterno",)
admin.site.register(Profesores, ProfesorAdmin)

class MateriaAdmin(admin.ModelAdmin):
  list_display = ("idMateria", "idProfesor", "nombreMateria", "horario",)
admin.site.register(Materias, MateriaAdmin)

class InscripcionAdmin(admin.ModelAdmin):
  list_display = ("idInscripcion", "idEstudiante", "idMateria", "costo",)
admin.site.register(Inscripciones, InscripcionAdmin)

class CalificacionAdmin(admin.ModelAdmin):
  list_display = ("idCalificacion", "idInscripcion", "parcial", "calificacion")
admin.site.register(Calificaciones, CalificacionAdmin)

class EventoAdmin(admin.ModelAdmin):
  list_display = ("idEvento", "tituloEvento", "hora", "dia", "lugar")
admin.site.register(Eventos, EventoAdmin)
