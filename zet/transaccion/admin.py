from django.contrib import admin
from transaccion.models import CompraProducto, CompraTotal, PedidoProducto, VentaTotal
from actions import export_as_csv


class CompraProductoAdmin(admin.ModelAdmin):
	list_display = ('producto','cantidad')
	list_filter = ('producto',)
	search_fields = ('producto','cantidad')
	actions = [export_as_csv]

class CompraTotalAdmin(admin.ModelAdmin):
	list_display = ('proveedor','fecha_compra','hora_compra')
	list_filter = ('proveedor',)
	search_fields = ('proveedor',)
	actions = [export_as_csv]

class PedidoProductoAdmin(admin.ModelAdmin):
	list_display = ('producto','cantidad')
	list_filter = ('producto',)
	search_fields = ('producto','cantidad')
	actions = [export_as_csv]

class VentaTotalAdmin(admin.ModelAdmin):
	list_display = ('cliente','fecha_venta','hora_venta','Total')
	list_filter = ('cliente',)
	search_fields = ('cliente',)
	actions = [export_as_csv]


admin.site.register(CompraProducto, CompraProductoAdmin)
admin.site.register(CompraTotal, CompraTotalAdmin)
admin.site.register(PedidoProducto, PedidoProductoAdmin)
admin.site.register(VentaTotal, VentaTotalAdmin)
