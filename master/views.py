from django.shortcuts import render, render_to_response
from .models import Alumno, Matricula 
# Create your views here.
def view_home(request):
	titulo="SISTEMA"
	consultanio= Matricula.objects.values("idalumno").filter(idano=2013,idgrado="11")
	consulta= Alumno.objects.filter(idalumno__in=consultanio)
	print consultanio
	print consulta
	ctx={"consulta":consulta, "titulo":titulo}
	return render_to_response("alumno/mostrar.html",ctx)