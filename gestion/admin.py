
from django.contrib import admin
from .models import Alumno, Materia

class AdminAlumno(admin.ModelAdmin):
	list_display =["cedula","nombre","apellido"]
	class Meta:
		model = Alumno
admin.site.register(Alumno,AdminAlumno)

class AdminMateria(admin.ModelAdmin):
	list_display = ["nombre","cupo","descripcion"]
	class Meta:
		model = Materia
admin.site.register(Materia,AdminMateria)