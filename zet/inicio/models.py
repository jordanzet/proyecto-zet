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

class Cajero(models.Model):
	dni = models.IntegerField(8)
	#dni = models.CharField(max_length=8)
	usuario = models.ForeignKey(User)
	avatar = models.FileField(upload_to=get_file_path, null=True)
	slug = models.CharField(max_length=10)
	status = models.CharField(max_length=8, choices=STATUS, default='active')

	def __unicode__(self):
		return self.usuario

	class Meta:
		db_table = "cajero"


class JefeInventario(models.Model):
	usuario = models.ForeignKey(User)
	avatar = models.FileField(upload_to=get_file_path, null=True)
	status = models.CharField(max_length=8, choices=STATUS, default='active')

	def __unicode__(self):
		return self.usuario

	class Meta:
		db_table = "jefe_proyecto"

		

