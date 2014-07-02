from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, response
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

def login_home(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')

				else:
					messages.add_message(request, messages.ERROR, "Datos incorrectos")
					return render_to_response(
						'inicio/login.html',
						context_instance=RequestContext(request)
					)
			else:
				messages.add_message(request, messages.ERROR, "Datos incorrectos")
				return render_to_response(
					'inicio/login.html',
					context_instance=RequestContext(request)
				)
	else :
		formulario = AuthenticationForm()
	return render_to_response(
		'inicio/login.html',
		{'formulario': formulario},
		context_instance=RequestContext(request)
	)

def logout_home(request):
	logout(request)
	return HttpResponseRedirect('/login')

def inicio(request):
	usuario = request.user
	return render_to_response('inicio/index.html',{'usuario': usuario},
		context_instance=RequestContext(request))


def estadisticas(request):
	usuario = request.user
	return render_to_response('inicio/estadisticas.html',{'usuario': usuario},
		context_instance=RequestContext(request))
