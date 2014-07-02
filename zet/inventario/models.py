from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import uuid, os

STATUS = [
	('active', 'Activo'),
	('inactive', 'Inactivo'),
	('delete', 'Eliminado')
]

def get_file_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	return os.path.join('uploads/avatar', filename)

class JefeInventario(models.Model):
	usuario = models.ForeignKey(User)
	dni = models.IntegerField()
	avatar = models.FileField(upload_to=get_file_path, null=True)
	telefono = models.IntegerField()
	status = models.CharField(max_length=8, choices=STATUS, default='active')

	def avatar(self):
		return 'http://localhost:8000/media/%s' %(self.avatar)

	def __unicode__(self):
		return unicode(self.usuario)

	class Meta:
		db_table = "jefe_inventario"

	#class Meta:
	#	db_table = "jefe_inventario"
		