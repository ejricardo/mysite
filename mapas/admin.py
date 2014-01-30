from django.contrib import admin
from mapas.models import *

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombreCategoria', 'nombreCategoria') 


		
admin.site.register(Mapa)
admin.site.register(Ubicacion)
admin.site.register(Categoria)
admin.site.register(Negocio)
admin.site.register(Lugar)
admin.site.register(Usuario)