# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from pessoa.forms import *
from pessoa.models import *

#Classe Pessoa
class PessoaList(ListView):
	"""
	View para listar participantes cadastrados.
	"""
	model = Pessoa
	template_name = 'pessoa/listar.html'

class PessoaNew(CreateView):
	"""
	View para a criação de novos participantes.
	"""
	model = Pessoa
	form_class = FormularioPessoa
	template_name = 'pessoa/novo.html'
	success_url = reverse_lazy('listar-participantes')

class PessoaEdit(UpdateView):
	"""
	View para a edição de participantes já cadastrados.
	"""
	model = Pessoa
	form_class = FormularioPessoa
	template_name = 'pessoa/editar.html'
	success_url = reverse_lazy('listar-participantes')

class PessoaDelete(DeleteView):
	"""
	View para a exclusão de participantes.
	"""
	model = Pessoa
	template_name = 'pessoa/deletar.html'
	success_url = reverse_lazy('listar-participantes')


#Classe Convocacao
class ConvocacaoList(ListView):
	"""
	View para listar convocacoes cadastradas.
	"""
	model = Convocacao
	template_name = 'pessoa/listarconvocacao.html'

class ConvocacaoNew(CreateView):
	"""
	View para a criação de novas convocacoes.
	"""
	model = Convocacao
	form_class = FormularioConvocacao
	template_name = 'pessoa/novaconvocacao.html'
	success_url = reverse_lazy('listar-convocacoes')

class ConvocacaoEdit(UpdateView):
	"""
	View para a edição de participantes já cadastrados.
	"""
	model = Convocacao
	form_class = FormularioConvocacao
	template_name = 'pessoa/editarconvocacao.html'
	success_url = reverse_lazy('listar-convocacoes')

class ConvocacaoDelete(DeleteView):
	"""
	View para a exclusão de convocacoes.
	"""
	model = Convocacao
	template_name = 'pessoa/deletarconvocacao.html'
	success_url = reverse_lazy('listar-convocacoes')