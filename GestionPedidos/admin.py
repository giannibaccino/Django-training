from django.contrib import admin
from GestionPedidos.models import Clientes,Articulos,Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=('nombre','direccion','telefono')
    search_fields=('nombre','telefono')
    
    
class ArticulosAdmin(admin.ModelAdmin):
    list_display=('nombre','seccion','precio')
    search_fields=('seccion','precio')
    list_filter=('seccion','precio',)
    
    
class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero','fecha','entregado')
    search_fields=('fecha','entregado')
    list_filter=('fecha',)
    ordering=('fecha',)
    date_hierarchy=('fecha')

admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos,ArticulosAdmin)
admin.site.register(Pedidos,PedidosAdmin)