from django.http import HttpResponse
from django.template import loader
from .models import Student, Estudiante, Profesores, Materias, Inscripciones, Calificaciones, Eventos

def students(request):
    mystudents = Student.objects.all().values()
    template = loader.get_template('all_students.html')
    context = {
        'mystudents': mystudents,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mystudent = Student.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mystudent': mystudent,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
    
def testing(request):
    mydata = Student.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mystudents': mydata,
    }
    return HttpResponse(template.render(context, request))

def estudiantes(request):
    myestudiantes = Estudiante.objects.all().values().order_by('idEstudiante').values()
    template = loader.get_template('estudiantes.html')
    context = {
        'myestudiantes': myestudiantes,
    }
    return HttpResponse(template.render(context, request))

def profesores(request):
    myprofesores = Profesores.objects.all().values().order_by('idProfesor').values()
    template = loader.get_template('profesores.html')
    context = {
        'myprofesores': myprofesores,
    }
    return HttpResponse(template.render(context, request))

def materias(request):
    mymaterias = Materias.objects.all().order_by('idMateria').values()
    profesores_ids = [materia['idProfesor_id'] for materia in mymaterias]
    profesores = Profesores.objects.filter(idProfesor__in=profesores_ids).values('idProfesor', 'nombre', 'apellidoPaterno', 'apellidoMaterno')
    profesores_data = {profesor['idProfesor']: profesor for profesor in profesores}
    for materia in mymaterias:
        profesor_id = materia['idProfesor_id']
        materia['nombre_profesor'] = f"{profesores_data[profesor_id]['nombre']} {profesores_data[profesor_id]['apellidoPaterno']} {profesores_data[profesor_id]['apellidoMaterno']}"
    template = loader.get_template('materias.html')
    context = {
        'mymaterias': mymaterias,
    }
    return HttpResponse(template.render(context, request))

def inscripciones(request):
    myinscripciones = Inscripciones.objects.all().order_by('idInscripcion').values()
    
    # Obtener los IDs de los estudiantes
    estudiantes_ids = [inscripcion['idEstudiante_id'] for inscripcion in myinscripciones]

    # Consultar los datos de los estudiantes
    estudiantes = Estudiante.objects.filter(idEstudiante__in=estudiantes_ids).values('idEstudiante', 'nombre', 'apellidoPaterno', 'apellidoMaterno')

    # Mapear los datos de los estudiantes usando el ID como clave
    estudiantes_data = {estudiante['idEstudiante']: estudiante for estudiante in estudiantes}

    # Agregar información de estudiantes a cada inscripción
    for inscripcion in myinscripciones:
        estudiante_id = inscripcion['idEstudiante_id']
        inscripcion['nombre_estudiante'] = f"{estudiantes_data[estudiante_id]['nombre']} {estudiantes_data[estudiante_id]['apellidoPaterno']} {estudiantes_data[estudiante_id]['apellidoMaterno']}"
    template = loader.get_template('inscripciones.html')
    context = {
        'myinscripciones': myinscripciones,
    }
    return HttpResponse(template.render(context, request))

def calificaciones(request):
    mycalificaciones = Calificaciones.objects.all().order_by('idCalificacion').values()
    
    # Obtener los IDs de las inscripciones
    inscripciones_ids = [calificacion['idInscripcion_id'] for calificacion in mycalificaciones]

    # Consultar los datos de las inscripciones
    inscripciones = Inscripciones.objects.filter(idInscripcion__in=inscripciones_ids).values('idInscripcion')

    # Mapear los datos de las inscripciones usando el ID como clave
    inscripciones_data = {inscripcion['idInscripcion']: inscripcion for inscripcion in inscripciones}

    # Agregar información de inscripciones a cada calificación
    for calificacion in mycalificaciones:
        inscripcion_id = calificacion['idInscripcion_id']
        calificacion['info_inscripcion'] = inscripciones_data.get(inscripcion_id, {}).get('idInscripcion') # Reemplaza 'campo_que_quieras_mostrar' con el campo que desees mostrar

    template = loader.get_template('calificaciones.html')
    context = {
        'mycalificaciones': mycalificaciones,
    }
    return HttpResponse(template.render(context, request))

def eventos(request):
    myeventos = Eventos.objects.all().order_by('idEvento').values()
    
    # Obtener los IDs de los profesores
    profesores_ids = [evento['idProfesor_id'] for evento in myeventos]

    # Consultar los datos de los profesores
    profesores = Profesores.objects.filter(idProfesor__in=profesores_ids).values('idProfesor', 'nombre', 'apellidoPaterno', 'apellidoMaterno')

    # Mapear los datos de los profesores usando el ID como clave
    profesores_data = {profesor['idProfesor']: profesor for profesor in profesores}

    # Agregar información de profesores a cada evento
    for evento in myeventos:
        profesor_id = evento['idProfesor_id']
        evento['nombre_profesor'] = f"{profesores_data[profesor_id]['nombre']} {profesores_data[profesor_id]['apellidoPaterno']} {profesores_data[profesor_id]['apellidoMaterno']}"

    template = loader.get_template('eventos.html')
    context = {
        'myeventos': myeventos,
    }
    return HttpResponse(template.render(context, request))