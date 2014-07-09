from django.contrib import admin
from producto.models import Proveedor,TipoProducto,AreaProducto,Producto,StockProducto
from actions import export_as_csv

	
class ProveedorAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'ruc','rubro')
	list_filter = ('nombre', 'ruc',)
	search_fields = ('nombre', 'ruc','rubro')
	actions = [export_as_csv]

		
class TipoProductoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'descripcion','area_producto')
	list_filter = (	'nombre', 'area_producto',)
	search_fields = ('nombre','descripcion', 'area_producto__ubicacion',)
	actions = [export_as_csv]


class AreaProductoAdmin(admin.ModelAdmin):
	list_display = ('id','ubicacion','nombre','descripcion')
	list_filter = ('ubicacion',)
	search_fields = ('ubicacion',)
	actions = [export_as_csv]


class ProductoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','descripcion','proveedor','tipo_producto','precio_compra','precio_venta','fecha_vencimiento')
	list_filter = ('nombre','proveedor','tipo_producto',)
	search_fields = ('tipo_producto__nombre','proveedor__nombre')
	actions = [export_as_csv]


class StockProductoAdmin(admin.ModelAdmin):
	list_display = ('id','producto','cantidad','fecha','hora')
	list_filter = ('producto',)
	search_fields = ('producto','cantidad')
	actions = [export_as_csv]


admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(AreaProducto, AreaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(StockProducto, StockProductoAdmin)