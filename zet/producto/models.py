from django.db import models
from datetime import datetime

class Proveedor(models.Model):
	nombre = models.CharField(max_length=12)
	ruc = models.IntegerField()

	def __unicode__(self):
		return self.nombre
	

class TipoProducto(models.Model):
	nombre = models.CharField(max_length=12)
	descripcion = models.TextField()

	def __unicode__(self):
		return self.nombre


class AreaProducto(models.Model):
	ubicacion = models.CharField(max_length=2)
	
	def __unicode__(self):
		return self.ubicacion


class Producto(models.Model):
	nombre = models.CharField(max_length=12)
	descripcion = models.TextField()
	proveedor = models.ManyToManyField(Proveedor)
	tipo_producto = models.ForeignKey(TipoProducto)
	area_producto = models.ForeignKey(AreaProducto)
	costo = models.FloatField()
	precio_unit = models.FloatField()
	fecha_vencimiento = models.DateField()

	def __unicode__(self):
		return self.nombre


class StockProducto(models.Model):

	cantidad = models.IntegerField()
	Producto = models.ForeignKey(Producto)

	def __unicode__(self):
		return "%s | %s" (self.Producto, self.cantidad)
	