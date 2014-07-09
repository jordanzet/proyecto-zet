from django.contrib import admin
from inventario.models import JefeInventario, CompraProducto, CompraTotal
from actions import export_as_csv


class JefeInventarioAdmin(admin.ModelAdmin):
	list_display = ('usuario','status',)
	list_filter = ('usuario',)
	search_fields = ('usuario__status',)
	actions = [export_as_csv]


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


admin.site.register(CompraProducto, CompraProductoAdmin)
admin.site.register(CompraTotal, CompraTotalAdmin)	
admin.site.register(JefeInventario, JefeInventarioAdmin)