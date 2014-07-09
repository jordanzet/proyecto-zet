from django.conf.urls import patterns, include, url
from inicio.views import *

urlpatterns = patterns('',
	url(r'login', 'inicio.views.login_home', name='login_home'),
	url(r'salir', 'inicio.views.logout_home', name='logout_home'),
	url(r'clientes','inicio.views.clientes', name='clientes'),

	url(r'calendario', 'inicio.views.calendario', name='calendario'),
	url(r'perfil','inicio.views.perfil', name='perfil'),
	url(r'esta','inicio.views.esta', name='esta'),
	url(r'galeria','inicio.views.galeria', name='galeria'),
	url(r'mensajes','inicio.views.mensajes', name='mensajes'),
	url(r'tablas','inicio.views.tablas', name='tablas'),
	url(r'invoice','inicio.views.invoice', name='invoice'),


	#Estadisticas
	url(r'estadisticas', 'inicio.views.estadisticas', name='estadisticas'),
	url(r'estadistica1', 'inicio.views.estadistica_clientes', name='es1'),
	url(r'estadistica2', 'inicio.views.estadistica_ventas_por_fecha', name='es2'),
	url(r'estadistica3', 'inicio.views.estadistica_ventas_cajero', name='es3'),
	url(r'estadistica4', 'inicio.views.estadistica_compras', name='es4')
)
