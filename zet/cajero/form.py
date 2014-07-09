from django.forms import ModelForm
from cajero.models import PedidoProducto, VentaTotal


class PedidoProductoForm(ModelForm):

	class Meta:
		model = PedidoProducto
	

class VentaTotalForm(ModelForm):

	class Meta:
		model = VentaTotal