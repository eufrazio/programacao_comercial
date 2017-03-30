# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from automoveis.forms import *

class AutomoveisList(ListView):
	"""
	View para listar automoveis cadastrados.
	"""
	model = Automovel
	form_class = FormularioAutomovel
	template_name = 'automoveis/listar.html'

class AutomoveisNew(CreateView):
	"""
	View para a criação de novos automoveis.
	"""
	model = Automovel
	form_class = FormularioAutomovel
	template_name = 'automoveis/novo.html'
	success_url = reverse_lazy('listar-automoveis')

class AutomoveisEdit(UpdateView):
	"""
	View para a edição de automoveis já cadastrados.
	"""
	model = Automovel
	form_class = FormularioAutomovel
	template_name = 'automoveis/editar.html'
	success_url = reverse_lazy('listar-automoveis')

class AutomoveisDelete(DeleteView):
	"""
	View para a exclusão de automoveis.
	"""
	model = Automovel
	template_name = 'automoveis/deletar.html'
	success_url = reverse_lazy('listar-automoveis')










































# 1. Codigo anterior
# from django.shortcuts import render
# from django.http import HttpResponse
# from automoveis.models import Automovel

# # Create your views here.

# def index(request):
# 	return HttpResponse(Automovel.objects.all())



# 2. Codigo anterior
# -*- coding: utf-8 -*-
# from django.views.generic import View
# from django.shortcuts import render
# from django.http import HttpResponse
# from automoveis.models import Automovel

# class AutomoveisList(View):
# 	"""
# 	View para listar automoveis cadastrados.
# 	"""
# 	def get(self, request):
# 		context = {
# 		'object_list': Automovel.objects.all().order_by('marca')
# 		}
# 		return render(request, 'automoveis/listar.html', context)

