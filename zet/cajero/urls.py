from django.conf.urls import patterns, include, url
from cajero.views import venta_cajero	

urlpatterns = patterns('',
	url(r'venta','cajero.views.venta_cajero', name='venta_cajero'),
)
