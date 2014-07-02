from django.conf.urls import patterns, include, url
from inventario.views import *

urlpatterns = patterns('',
	# urls cajeros 
	#url(r'', 'inventario.views.inventario', name='inventario'),

	url(r'agregar-producto', 'inventario.views.agregar_producto', name='addproducto'),
	url(r'actualizar-stock-producto', 'inventario.views.actualizar_stock_producto', name='actualizar-producto'),
	url(r'eliminar-producto/$', 'inventario.views.eliminar_producto', name='deleteproducto'),
	url(r'agregar-proveedor', 'inventario.views.agregar_proveedor', name='addproveedor'),
	url(r'actualizar-proveedor', 'inventario.views.actualizar_provedor', name='actualizar-proveedor'),
	url(r'eliminar-proveedor', 'inventario.views.eliminar_provedor', name='deleteproveedor'),

	#url(r'cajero','inicio.views.cajero', name='cajero'),
	#url(r'cajero/boleta','inicio.views.boleta', name='boleta'),
	#url(r'nosotros','inicio.views.nosotros', name='nosotros'),
)



