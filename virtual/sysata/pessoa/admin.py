from django.contrib import admin
from pessoa.models import *

class PessoaAdmin(admin.ModelAdmin):
	"""
	Admin para o model Pessoa
	"""
	list_display = ['nome', 'cpf', 'telefone', 'email', 'departamento']
	search_fields = ['nome', 'cpf']
	list_filter = ['cpf']
admin.site.register(Pessoa, PessoaAdmin)