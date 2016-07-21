from rest_framework import serializers
from gestion.models import Alumno
from gestion.models import Materia


class AlumnoSerializable(serializers.ModelSerializer):
	class Meta:
		model = Alumno
		fields = ["cedula","nombre","apellido"]

class MateriaSerializable(serializers.ModelSerializer):
	class Meta:
		model = Materia 
		fields = ["nombre","cupo","descripcion"]


