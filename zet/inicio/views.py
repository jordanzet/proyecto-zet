# -*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, response
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from inicio.models import Cliente


def login_home(request):
	if not request.user.is_anonymous():
		groupUser = request.user.groups.all()[0].name
		if groupUser == 'administrador':
			return HttpResponseRedirect('/admin')
		elif groupUser == 'cajero':
			return HttpResponseRedirect('/cajero')
		elif groupUser == 'dueño' :
			return HttpResponseRedirect('/admin')
		elif groupUser == 'gerente_de_tienda' :
			return HttpResponseRedirect('/admin')
		elif groupUser == 'jefe_de_inventario' :
			return HttpResponseRedirect('/inventario')
		elif groupUser == 'mantenimiento_de_software' :
			return HttpResponseRedirect('/admin')

	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					groupUser = user.groups.all()[0].name
					if groupUser == 'administrador':
						return HttpResponseRedirect('/admin')
					elif groupUser == 'cajero':
						return HttpResponseRedirect('/cajero')
					elif groupUser == 'dueño' :
						return HttpResponseRedirect('/admin')
					elif groupUser == 'gerente_de_tienda' :
						return HttpResponseRedirect('/admin')
					elif groupUser == 'jefe_de_inventario' :
						return HttpResponseRedirect('/inventario')
					elif groupUser == 'mantenimiento_de_software' :
						return HttpResponseRedirect('/admin')
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

@login_required 
def inicio(request):
	usuario = request.user
	return render_to_response('inicio/index.html',{'usuario': usuario},
		context_instance=RequestContext(request))

def estadisticas(request):
	usuario = request.user
	return render_to_response('inicio/estadisticas.html',{'usuario': usuario},
		context_instance=RequestContext(request))

def clientes(request):
	usuario = request.user
	lista_de_clientes = Cliente.objects.all()

	return render_to_response('inicio/lista_de_clientes.html',{'usuario': usuario,'lista_de_clientes':lista_de_clientes},
		context_instance=RequestContext(request))

def estadistica_clientes(request):
	pass

#estadisticas de ventas del cajero
def estadistica_ventas_por_fecha(request):
	pass

def estadistica_ventas_cajero(request):
	pass

#estadisticas de compras
def estadistica_compras(request):
	pass

#estadisticas de ventas
def estadistica_ventas_cajero(request):
	pass






