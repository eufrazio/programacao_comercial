from django.contrib import admin
from pessoa.models import *

class PessoaAdmin(admin.ModelAdmin):
	"""
	Admin para o model Pessoa
	"""
	list_display = ['nome', 'cpf', 'telefone', 'email', 'departamento']
	search_fields = ['nome', 'cpf']
	list_filter = ['cpf']

class ConvocacaoAdmin(admin.ModelAdmin):
	"""
	Admin para o model Convocacao
	"""
	list_display = ['tema', 'data_convocacao']
	search_fields = ['tema']
	list_filter = ['tema']

class MembroAdmin(admin.ModelAdmin):
	"""
	Admin para o model Convocacao
	"""
	list_display = ['nome_pessoa', 'participacao', 'tema_convocacao', 'data_membro']
	search_fields = ['tema']
	list_filter = ['nome_pessoa', 'tema_convocacao']

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Convocacao, ConvocacaoAdmin)
admin.site.register(Membro, MembroAdmin)


