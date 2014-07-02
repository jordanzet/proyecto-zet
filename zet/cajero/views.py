from django.template import RequestContext
from django.shortcuts import render, render_to_response


def venta_cajero(request):
	usuario = request.user
	return render_to_response(
		'cajero/venta.html',
		{'usuario': usuario},
		context_instance=RequestContext(request))

def index(request):
	usuario = request.user
	return render_to_response(
		'cajero/index.html',
		{'usuario': usuario},
		context_instance=RequestContext(request))

