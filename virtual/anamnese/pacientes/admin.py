from django.contrib import admin
from pacientes.models import *
class PacienteAdmin(admin.ModelAdmin):
	'''
	Admin para o model Paciente
	'''
	list_display = ['nome', 'idade', 'sexo', 'profissao', 'alergia']
	search_fields = ['nome', 'alergia']
	list_filter = ['uso_medicamento']


admin.site.register(Paciente, PacienteAdmin)


#from django.contrib import admin

# Register your models here.