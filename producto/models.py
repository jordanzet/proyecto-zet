from django.db import models
from datetime import datetime

class Proveedor(models.Model):
	nombre = models.CharField(max_length=50)
	ruc = models.IntegerField()
	rubro = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre
 

class AreaProducto(models.Model):
	ubicacion = models.CharField(max_length=2)
	nombre = models.CharField(max_length=140)
	descripcion = models.TextField()
	
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
	fecha = models.DateField(auto_now_add=True)
	hora = models.TimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.cantidad)


