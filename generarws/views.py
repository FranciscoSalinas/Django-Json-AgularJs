from gestion.models import Alumno
from gestion.models import Materia
from rest_framework import viewsets
from .serializable import AlumnoSerializable
from .serializable import MateriaSerializable

class AlumnoViewSet(viewsets.ModelViewSet):
	serializer_class = AlumnoSerializable
	queryset = Alumno.objects.all()

class MateriaViewSet(viewsets.ModelViewSet):
	serializer_class = MateriaSerializable
	queryset = Materia.objects.filter(cupo__gt=0,cupo__lte=30)

