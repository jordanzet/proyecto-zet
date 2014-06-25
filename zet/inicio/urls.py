from django.conf.urls import patterns, include, url
from inicio.views import cajero, login_home, logout_home, estadisticas, jefe_inventario 

urlpatterns = patterns('',
	url(r'cajero','inicio.views.cajero', name='cajero'),
	url(r'login', 'inicio.views.login_home', name='login_home'),
	url(r'salir', 'inicio.views.logout_home', name='logout_home'),
	url(r'estadisticas', 'inicio.views.estadisticas', name='estadisticas'),
	url(r'jefe_inventario', 'inicio.views.jefe_inventario', name='jefe_inventario'),
	#url(r'nosotros','inicio.views.nosotros', name='nosotros'),
)
