from django.db import models
from producto.models import Producto
from django.contrib.auth.models import User

STATUS = [
	('activo', 'Activo'),
	('inactivo', 'Inactivo'),
	('despedido', 'despedido')
] 


class Cajero(models.Model):
	usuario = models.ForeignKey(User)
	dni = models.IntegerField()
	telefono = models.IntegerField()
	status = models.CharField(max_length=8, choices=STATUS, default='activo')

	def __unicode__(self):
		return unicode(self.usuario)


#class PedidoUnitario(models.Model):
#	cantidad = models.IntegerField()
#	producto = models.ForeignKey(Producto)



#class PedidoTotal(models.Model):
#	cantidad = models.IntegerField()
#	producto = models.ForeignKey(Producto)




