from django.db import models
from datetime import datetime
from producto.models import Producto, Proveedor
from inicio.models import Cliente

class CompraProducto(models.Model):
	producto = models.ForeignKey(Producto)
	cantidad = models.IntegerField()
 
	def __unicode__(self):
		return self.producto

 
class CompraTotal(models.Model):
	proveedor = models.ForeignKey(Proveedor)
	fecha_compra = models.DateField(auto_now_add=True)
	hora_compra = models.TimeField(auto_now_add=True)
	Total_compra = models.FloatField()
	igv = models.FloatField(default=18)
	lista_de_compra = models.ManyToManyField(CompraProducto)

	def __unicode__(self):
		return unicode(self.proveedor)


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

