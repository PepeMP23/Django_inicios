from django.db import models

class Estudiante(models.Model):
    idEstudiante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellidoPaterno = models.CharField(max_length=255)
    apellidoMaterno = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.idEstudiante} {self.nombre} {self.apellidoPaterno} {self.apellidoMaterno}"
    
class Profesores(models.Model):
    idProfesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellidoPaterno = models.CharField(max_length=255)
    apellidoMaterno = models.CharField(max_length=255)
    fechaContratacion = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "Profesores"

    def __str__(self):
        return f"{self.idProfesor} {self.nombre} {self.apellidoPaterno} {self.apellidoMaterno}"
    
class Materias(models.Model):
    idMateria = models.AutoField(primary_key=True)
    idProfesor = models.ForeignKey(Profesores, on_delete=models.CASCADE)
    nombreMateria = models.CharField(max_length=255)
    horario = models.CharField(max_length=255)
    creditos = models.IntegerField()

    class Meta:
        verbose_name_plural = "Materias"

    def __str__(self):
        return f"{self.idMateria} {self.nombreMateria}"
    
class Inscripciones(models.Model):
    idInscripcion = models.AutoField(primary_key=True)
    idEstudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    idMateria = models.ForeignKey(Materias, on_delete=models.CASCADE)
    costo = models.IntegerField()

    class Meta:
        verbose_name_plural = "Inscripciones"

    def __str__(self):
        return f"{self.idInscripcion} {self.idEstudiante} {self.idMateria} {self.costo}"

class Calificaciones(models.Model):
    idCalificacion = models.AutoField(primary_key=True)
    idInscripcion = models.ForeignKey(Inscripciones, on_delete=models.CASCADE)
    parcial = models.IntegerField()
    calificacion = models.IntegerField()

    class Meta:
        verbose_name_plural = "Calificaciones"

    def __str__(self):
        return f"{self.idCalificacion} {self.idInscripcion} {self.parcial} {self.calificacion}"
    
class Eventos(models.Model):
    idEvento = models.AutoField(primary_key=True)
    idProfesor = models.ForeignKey(Profesores, on_delete=models.CASCADE)
    tituloEvento = models.CharField(max_length=255)
    dia = models.DateField(null=True)
    hora = models.TimeField(null=True)
    lugar = models.CharField(max_length=255) 

    class Meta:
        verbose_name_plural = "Eventos"

    def __str__(self):
        return f"{self.idEvento} {self.idProfesor} {self.tituloEvento} {self.dia} {self.hora} {self.lugar}"
    

class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField()
    joined_date = models.DateField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"