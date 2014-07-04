from django.forms import ModelForm
from producto.models import Producto, Proveedor
	
class ProductoForm(ModelForm):
	
	class Meta:
		model = Producto
	

class ProveedorForm(ModelForm):

    class Meta:
        model = Proveedor
    
														