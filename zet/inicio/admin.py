from django.contrib import admin
from inicio.models import Cliente
from actions import export_as_csv

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('id','usuario','ruc','telefono','nivel_de_fidelidad')
	list_filter = ('usuario',)	
	actions = [export_as_csv]

admin.site.register(Cliente, ClienteAdmin)