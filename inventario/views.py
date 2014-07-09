from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, response
from inventario.form import ProductoForm, ProveedorForm, AreaProductoForm, TipoProductoForm, StockProductoForm
from producto.models import  Producto, Proveedor, AreaProducto, TipoProducto, StockProducto

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

@login_required
def agregar_area_producto(request):
	if request.method == 'POST':
		# formulario enviado
		area_producto_form = AreaProductoForm(request.POST)
		if area_producto_form.is_valid():
			area_producto_form.save()
			return HttpResponseRedirect('/inventario/agregar-area-producto')
	else:
		area_producto_form = AreaProductoForm()

	list_area_producto = AreaProducto.objects.all()
	template = 'inventario/agregar_area_producto.html'
	return render_to_response(
		template, 
		{ 'area_producto_form': area_producto_form,'list_area_producto':list_area_producto}, 
		context_instance=RequestContext(request))

@login_required
def agregar_tipo_producto(request):
	if request.method == 'POST':
		# formulario enviado
		tipo_producto_form = TipoProductoForm(request.POST)
		if tipo_producto_form.is_valid():
			tipo_producto_form.save()
			return HttpResponseRedirect('/inventario/agregar-tipo-producto')
	else:
		tipo_producto_form = TipoProductoForm()

	list_tipo_producto = TipoProducto.objects.all()
	template = 'inventario/agregar_tipo_producto.html'
	return render_to_response(
		template, 
		{ 'tipo_producto_form': tipo_producto_form,'list_tipo_producto':list_tipo_producto}, 
		context_instance=RequestContext(request))

@login_required
def agregar_stock_producto(request):
	if request.method == 'POST':
		# formulario enviado
		stock_producto_form = StockProductoForm(request.POST)
		if stock_producto_form.is_valid():
			stock_producto_form.save()
			return HttpResponseRedirect('/inventario/agregar-stock-producto')
	else:
		stock_producto_form = StockProductoForm()

	list_stock_producto = StockProducto.objects.all()
	template = 'inventario/agregar_stock_producto.html'
	return render_to_response(
		template, 
		{ 'stock_producto_form': stock_producto_form,'list_stock_producto':list_stock_producto}, 
		context_instance=RequestContext(request))

# OTROS
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





