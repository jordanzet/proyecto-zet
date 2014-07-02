from django.contrib import admin
from inventario.models import JefeInventario
from actions import export_as_csv


class JefeInventarioAdmin(admin.ModelAdmin):
	list_display = ('usuario','status',)
	list_filter = ('usuario',)
	search_fields = ('usuario__status',)
	#list_editable = ('titulo', 'enlace', 'categoria')
	#list_display_links = ('es_popular',)
	actions = [export_as_csv]
	#raw_id_fields = ('categoria', 'usuario')

	
admin.site.register(JefeInventario, JefeInventarioAdmin)
