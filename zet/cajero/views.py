from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, response
from cajero.form import VentaTotalForm, PedidoProductoForm
from cajero.models import VentaTotal, PedidoProducto


def index(request):
	usuario = request.user
	return render_to_response(
		'cajero/index.html',
		{'usuario': usuario},
		context_instance=RequestContext(request))


@login_required
def venta_cajero(request):
	if request.method == 'POST':
		# formulario enviado
		pedido_producto_form = PedidoProductoForm(request.POST)
		if pedido_producto_form.is_valid():
			pedido_producto_form.save()
			return HttpResponseRedirect('/cajero/venta')
	else:
		pedido_producto_form = PedidoProductoForm()

	list_pedido_producto = PedidoProducto.objects.all()
	template = 'cajero/venta.html'
	return render_to_response(
		template, 
		{ 'pedido_producto_form': pedido_producto_form,'list_pedido_producto':list_pedido_producto}, 
		context_instance=RequestContext(request))


