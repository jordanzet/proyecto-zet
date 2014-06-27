from django.conf.urls import patterns, include, url
#from inicio.views import cajero, login_home, logout_home, estadisticas, jefe_inventario 
from cajero.views import venta_cajero	

urlpatterns = patterns('',
	url(r'venta','cajero.views.venta_cajero', name='venta_cajero'),
	#url(r'nosotros','inicio.views.nosotros', name='nosotros'),
)
