from django.contrib import admin
from producto.models import Proveedor, TipoProducto,AreaProducto,Producto,StockProducto


admin.site.register(Proveedor)
admin.site.register(TipoProducto)
admin.site.register(AreaProducto)
admin.site.register(Producto)
admin.site.register(StockProducto)