from django.conf.urls import patterns, include, url
from inicio.views import *
#from inicio.views import cajero,login_home,logout_home,estadisticas,inventario

urlpatterns = patterns('',
	url(r'login', 'inicio.views.login_home', name='login_home'),
	url(r'salir', 'inicio.views.logout_home', name='logout_home'),
	url(r'estadisticas', 'inicio.views.estadisticas', name='estadisticas'),
	#url(r'nosotros','inicio.views.nosotros', name='nosotros'),
)
