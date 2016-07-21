from django import forms
from .models import Alumno
from .models import Materia

class FormularioAlumno(forms.ModelForm):
	class Meta:
		model = Alumno
		fields=["cedula","nombre","apellido"]

class FormularioMateria(forms.ModelForm):
	class Meta:
		model = Materia
		fields=["nombre","cupo","descripcion"]


class FormularioModificarAlumno(forms.ModelForm):
	class Meta:
		model = Alumno
		fields=["nombre","apellido"]

class FormularioModificarMateria(forms.ModelForm):
	class Meta:
		model = Materia
		fields=["cupo","descripcion"]