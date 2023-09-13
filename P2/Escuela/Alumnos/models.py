from django.db import models

class Alumno(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=255)
