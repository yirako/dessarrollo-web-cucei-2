from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Template

from .models import Usuario, UsuarioForm

# Create your views here.
def index(request):
	if request.method == 'POST':
		formulario = UsuarioForm(request.POST)

		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/gracias/')
	else:
		formulario = UsuarioForm()

	template = loader.get_template('formularios/index.html')
	context = RequestContext(request, {
		'formulario': formulario,
	})
	return HttpResponse(template.render(context))

def registrado(request):
	template = Template("<html><body>{{ debug }}<h1>Gracias por tu registro</h1></body></html>")
	context = RequestContext(request, {
		'debug': Usuario.objects.all()
	})
	return HttpResponse(template.render(context))