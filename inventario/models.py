from django.db import models
from django.contrib.auth.models import User
from producto.models import Producto, Proveedor

STATUS = [
	('activo', 'Activo'),
	('inactivo', 'Inactivo'),
	('despedido', 'despedido')
]

class JefeInventario(models.Model):
	usuario = models.ForeignKey(User)
	dni = models.IntegerField()
	telefono = models.IntegerField()
	status = models.CharField(max_length=8, choices=STATUS, default='activo')

	def __unicode__(self):
		return unicode(self.usuario)


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
 