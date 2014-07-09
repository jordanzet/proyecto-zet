from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# ADMIN
	url(r'^admin/', include(admin.site.urls)),

	#Inicio
	url(r'^$', 'inicio.views.inicio', name='inicio'),
	url(r'^', include('inicio.urls')),

	# CAJERO
	url(r'^cajero/',include('cajero.urls')),
	url(r'^cajero$', 'cajero.views.index', name='cajero'),
	
	# INVENTARIO
	url(r'^inventario$', 'inventario.views.inventario', name='inventario'),
	url(r'^inventario/', include('inventario.urls')),
	
)	 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
