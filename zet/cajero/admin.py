from django.contrib import admin
from cajero.models import Cajero, PedidoProducto, VentaTotal
from actions import export_as_csv

class CajeroAdmin(admin.ModelAdmin):
	list_display = ('id','usuario','dni','status',)
	list_filter = ('usuario','dni',)
	search_fields = ('usuario__status','usuario__dni',)
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


admin.site.register(Cajero,CajeroAdmin)
admin.site.register(PedidoProducto, PedidoProductoAdmin)
admin.site.register(VentaTotal, VentaTotalAdmin)


