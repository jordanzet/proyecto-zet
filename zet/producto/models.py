from django.db import models
from datetime import datetime

class Proveedor(models.Model):
	nombre = models.CharField(max_length=12)
	ruc = models.IntegerField()

	def __unicode__(self):
		return self.nombre
 

class AreaProducto(models.Model):
	ubicacion = models.CharField(max_length=2)
	
	def __unicode__(self):
		return self.ubicacion


class TipoProducto(models.Model):
	nombre = models.CharField(max_length=12)
	descripcion = models.TextField()
	area_producto = models.ForeignKey(AreaProducto)

	def __unicode__(self):
		return self.nombre


class Producto(models.Model):
	nombre = models.CharField(max_length=12)
	descripcion = models.TextField()
	proveedor = models.ForeignKey(Proveedor)
	tipo_producto = models.ForeignKey(TipoProducto)
	precio_compra = models.FloatField()
	precio_venta = models.FloatField()
	fecha_vencimiento = models.DateField()

	def __unicode__(self):
		return self.nombre


class StockProducto(models.Model):
	producto = models.ForeignKey(Producto)
	cantidad = models.IntegerField()

	def __unicode__(self):
		return "%s | %s" (self.Producto, self.cantidad)


