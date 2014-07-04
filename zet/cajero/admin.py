from django.contrib import admin
from cajero.models import Cajero
from actions import export_as_csv


class CajeroAdmin(admin.ModelAdmin):
	list_display = ('usuario','dni','status',)
	list_filter = ('usuario','dni',)
	search_fields = ('usuario__status','usuario__dni',)
	actions = [export_as_csv]

admin.site.register(Cajero,CajeroAdmin)

