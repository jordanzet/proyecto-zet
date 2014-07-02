from django.contrib import admin
from producto.models import Proveedor, TipoProducto,AreaProducto,Producto,StockProducto


class ProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion','tipo_producto','area_producto','costo','precio_unit','fecha_vencimiento')
	list_filter = ('nombre','tipo_producto','area_producto',)
	search_fields = ('tipo_producto__nombre',)


admin.site.register(Proveedor)
admin.site.register(TipoProducto)
admin.site.register(AreaProducto)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(StockProducto)