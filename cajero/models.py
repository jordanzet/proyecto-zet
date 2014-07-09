from django.db import models
from producto.models import Producto
from inicio.models import Cliente
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



class PedidoProducto(models.Model):
	producto = models.ForeignKey(Producto)
	cantidad = models.IntegerField()	

	def __unicode__(self):
		return "%i | %s " %(self.cantidad, self.producto)
	

class VentaTotal(models.Model):
	cliente = models.ForeignKey(Cliente)
	fecha_venta = models.DateField(auto_now_add=True)
	hora_venta = models.TimeField(auto_now_add=True)
	Total = models.FloatField()
	lista_pedido = models.ManyToManyField(PedidoProducto)

	def __unicode__(self):
		return self.cliente

