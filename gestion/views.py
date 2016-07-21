from django.shortcuts import render, redirect
from .models import Alumno, Materia
from .forms import FormularioAlumno, FormularioMateria, FormularioModificarAlumno, FormularioModificarMateria

# Create your views here.
def listar(request):
	alumno = Alumno.objects.all()
	materia = Materia.objects.all()
	context={
		'alumno': alumno,
		'materia': materia,
	}
	return render(request,"listar.html",context)

def NuevoEstudiante(request):
	f = FormularioAlumno(request.POST or None)

	if request.method == 'POST':
		if f.is_valid():
			f_data = f.cleaned_data
			e = Alumno()
			e.cedula = f_data.get("cedula")
			e.nombre = f_data.get("nombre")
			e.apellido = f_data.get("apellido")
			if(e.save()!=True):
				return redirect(listar)
	context = {
		'f':f,
	}
	return render(request,"CrearEstudiante.html",context)

def NuevaMateria(request):
	f = FormularioMateria(request.POST or None)

	if request.method=="POST":
		if f.is_valid():
			f_data = f.cleaned_data
			m = Materia()
			m.nombre = f_data.get("nombre")
			m.cupo = f_data.get("cupo")
			m.descripcion= f_data.get("descripcion")
			if(m.save()!=True):
				return redirect(listar)
	context = {
		'f':f,
	}
	return render(request,"CrearMateria.html",context)


def ModificarEstudiante(request):
	est = Alumno.objects.get(cedula=request.GET['cedula'])
	f = FormularioModificarAlumno(request.POST or None)

	f.fields["nombre"].initial = est.nombre
	f.fields["apellido"].initial = est.apellido

	if f.is_valid():
		f_data = f.cleaned_data
		est.nombre = f_data.get("nombre")
		est.apellido = f_data.get("apellido")
		est.save()
		return redirect(listar)

	context = {
		'est':est,
		'f':f,
	}
	return render(request,"ModificarEstudiante.html",context)

def ModificarMateria(request):
	mat = Materia.objects.get(nombre=request.GET['nombre'])
	f = FormularioModificarMateria(request.POST or None)

	f.fields["cupo"].initial = mat.cupo
	if f.is_valid():
		f_data = f.cleaned_data
		mat.cupo = f_data.get("cupo")
		mat.save()
		return redirect(listar)
	context={
		'mat':mat,
		'f':f,
	}
	return render(request,"ModificarMateria.html",context)

def EliminarEstudiante(request):
	est = Alumno.objects.get(cedula=request.GET['cedula'])
	est.delete()
	return redirect(listar)

def EliminarMateria(request):
	mat = Materia.objects.get(nombre=request.GET['nombre'])
	mat.delete()
	return redirect(listar)