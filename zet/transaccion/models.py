from django.db import models
from datetime import datetime
from producto.models import Producto


class Compra(models.Model):
	proveedor = models.CharField(max_length=12)
	ruc = models.IntegerField()
	fecha = models.DateTimeField(auto_now=True)
	Total_compra = models.FloatField()
	igv = models.FloatField() 

	def __unicode__(self):
		return self.proveedor


class PedidoUnitario(models.Model):
	cantidad = models.IntegerField()
	producto = models.ForeignKey(Producto)

	def __unicode__(self):
		return "%i | %s " %(self.cantidad, self.producto)
	
 
class ListaPedido(models.Model):
	costa_total = models.FloatField()
	pedido = models.ManyToManyField(PedidoUnitario)

	def __unicode__(self):
		return self.costa_total
	

class Venta(models.Model):
	cliente = models.CharField(max_length=12)
	ruc = models.IntegerField()
	fecha = models.DateTimeField()
	Total = models.FloatField()
	lista_pedido = models.ForeignKey(ListaPedido)

	def __unicode__(self):
		return self.cliente
