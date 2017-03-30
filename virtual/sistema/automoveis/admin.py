from django.contrib import admin
from automoveis.models import *

# Register your models here.

class AutomovelAdmin(admin.ModelAdmin):
	"""
	Admin para o model Automovel
	"""
	list_display = ['marca', 'modelo', 'ano_fabricacao', 'modelo_fabricacao', 'combustivel']
	search_fields = ['marca', 'modelo']
	list_filter = ['combustivel']
admin.site.register(Automovel, AutomovelAdmin)