from django.contrib import admin
from inicio.models import Cliente
from actions import export_as_csv

class ClienteAdmin(admin.ModelAdmin):
	pass
	#list_display = 




admin.site.register(Cliente)