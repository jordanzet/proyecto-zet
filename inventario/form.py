from django.forms import ModelForm
from producto.models import Producto, Proveedor,AreaProducto,TipoProducto,StockProducto
from inventario.models import CompraProducto, CompraTotal

	
class ProductoForm(ModelForm):
	
	class Meta:
		model = Producto
	

class ProveedorForm(ModelForm):

	class Meta:
		model = Proveedor


class AreaProductoForm(ModelForm):
	
	class Meta:
		model = AreaProducto

	
class TipoProductoForm(ModelForm):
	
	class Meta:
		model = TipoProducto
	

class StockProductoForm(ModelForm):
	
	class Meta:
		model = StockProducto


class CompraProductoForm(ModelForm):

	class Meta:
		model = CompraProducto	


class CompraTotalForm(ModelForm):

	class Meta:
		model = CompraTotal