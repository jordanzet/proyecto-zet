from django.db import models
from producto.models import Producto
from django.contrib.auth.models import User
import uuid, os

STATUS = [
	('activo', 'Activo'),
	('inactivo', 'Inactivo'),
	('despedido', 'despedido')
]

def get_file_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	return os.path.join('uploads/cajeros/', filename)

class Cajero(models.Model):
	usuario = models.ForeignKey(User)
	dni = models.IntegerField()
	avatar = models.FileField(upload_to=get_file_path, null=True)
	telefono = models.IntegerField()
	status = models.CharField(max_length=8, choices=STATUS, default='activo')

	def avatar(self):
		return 'http://localhost:8000/media/%s' %(self.avatar)

	def __unicode__(self):
		return unicode(self.usuario)

	class Meta:
		db_table = "cajero"


#class PedidoUnitario(models.Model):
#	cantidad = models.IntegerField()
#	producto = models.ForeignKey(Producto)



#class PedidoTotal(models.Model):
#	cantidad = models.IntegerField()
#	producto = models.ForeignKey(Producto)




