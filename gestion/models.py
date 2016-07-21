from django.db import models


class Alumno(models.Model):
	cedula = models.CharField(max_length=10, unique=True)
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)

	def __str__(self):
		return self.cedula

class Materia(models.Model):
	nombre = models.CharField(max_length=30,unique=True)
	cupo = models.IntegerField()
	descripcion = models.TextField(max_length=150,default="descripcion")

	def __str__(self):
		return self.nombre