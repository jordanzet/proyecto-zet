from django.shortcuts import render

# Create your views here.
def venta_cajero(request):
	usuario = request.user
	return render_to_response('inicio/venta_cajero.html',{'usuario': usuario},
		context_instance=RequestContext(request))