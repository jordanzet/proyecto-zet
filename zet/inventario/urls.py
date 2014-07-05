from django.conf.urls import patterns, include, url
from inventario.views import *

urlpatterns = patterns('',
	url(r'actualizar-stock-producto', 'inventario.views.actualizar_stock_producto', name='actualizar-producto'),
	url(r'eliminar-producto/$', 'inventario.views.eliminar_producto', name='deleteproducto'),
	url(r'actualizar-proveedor', 'inventario.views.actualizar_provedor', name='actualizar-proveedor'),
	url(r'eliminar-proveedor', 'inventario.views.eliminar_provedor', name='deleteproveedor'),

	# Agregados del Inventario
	url(r'agregar-producto', 'inventario.views.agregar_producto', name='addproducto'),
	url(r'agregar-proveedor', 'inventario.views.agregar_proveedor', name='addproveedor'),
	url(r'agregar-area-producto', 'inventario.views.agregar_area_producto', name='add-area-producto'),
	url(r'agregar-tipo-producto', 'inventario.views.agregar_tipo_producto', name='add-tipo-producto'),
	url(r'agregar-stock-producto', 'inventario.views.agregar_stock_producto', name='add-stock-producto'),
)



