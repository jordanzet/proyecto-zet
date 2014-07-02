from django.contrib import admin
from cajero.models import Cajero
from actions import export_as_csv


class CajeroAdmin(admin.ModelAdmin):
	list_display = ('usuario','dni','status','avatar_cajero')
	list_filter = ('usuario','dni',)
	search_fields = ('usuario__status','usuario__dni',)
	actions = [export_as_csv]

	def avatar_cajero(self, obj):
		url = obj.avatar()
		tag = '<img width="130px" src="%s">' %url
		return tag

	avatar_cajero.allow_tags = True

admin.site.register(Cajero,CajeroAdmin)

