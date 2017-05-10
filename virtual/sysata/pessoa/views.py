# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
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

	#Função para envio de e-mails
	def send_mail(self):
		for convocado in Convocacao.objects.all():
			send_mail(convocado.tema, convocado.pauta, settings.DEFAULT_FROM_EMAIL, convocado.email)
			# send_mail(subject, message, from_email, user.Email)
	#CONFIGURAR ESSA FUNCAOsend_mail()

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