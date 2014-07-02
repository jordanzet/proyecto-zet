from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, response
#from django.contrib import messages
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import login, authenticate, logout
from inventario.form import ProductoForm, ProveedorForm
from producto.models import  Producto, Proveedor

def inventario(request):
	usuario = request.user
	return render_to_response(
		'inventario/inventario.html',
		{'usuario': usuario},
		context_instance=RequestContext(request))

@login_required
def agregar_producto(request):
	if request.method == 'POST':
		# formulario enviado
		producto_form = ProductoForm(request.POST)
		if producto_form.is_valid():
			producto_form.save()
			return HttpResponseRedirect('/inventario/agregar-producto')
	else:
		producto_form = ProductoForm()

	list_producto = Producto.objects.all()
	template = 'inventario/agregar_producto.html'
	return render_to_response(
		template, 
		{ 'producto_form': producto_form,'list_producto':list_producto}, 
		context_instance=RequestContext(request))

@login_required
def agregar_proveedor(request):
	if request.method == 'POST':
		# formulario enviado
		proveedor_form = ProveedorForm(request.POST)
		if proveedor_form.is_valid():
			proveedor_form.save()
			return HttpResponseRedirect('/inventario/agregar-proveedor')
	else:
		proveedor_form = ProveedorForm()

	list_proveedor = Proveedor.objects.all()
	template = 'inventario/agregar_proveedor.html'
	return render_to_response(
		template, 
		{ 'proveedor_form': proveedor_form,'list_proveedor':list_proveedor}, 
		context_instance=RequestContext(request))


def actualizar_stock_producto(request):
	usuario = request.user
	return render_to_response(
		'inventario/actualizar_stock_producto.html',
		{'usuario': usuario},
		context_instance=RequestContext(request))

def eliminar_producto(request):
	usuario = request.user
	return render_to_response(
		'inventario/eliminar_producto.html',
		{'usuario': usuario},
		context_instance=RequestContext(request))

def actualizar_provedor(request):
	usuario = request.user
	return render_to_response(
		'inventario/actualizar_provedor.html',
		{'usuario': usuario},
		context_instance=RequestContext(request))

def eliminar_provedor(request):
	usuario = request.user
	return render_to_response(
		'inventario/eliminar_provedor.html',
		{'usuario': usuario},
		context_instance=RequestContext(request))





