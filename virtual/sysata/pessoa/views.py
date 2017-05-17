# -*- coding: utf-8 -*-
from django.views.generic.edit import ModelFormMixin
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
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
	# def send_mail(self):
	# conv = Convocacao()
	# pess = Pessoa()
	# # for convocado in Convocacao.objects.all():
	# send_mail(conv.tema, conv.pauta, settings.DEFAULT_FROM_EMAIL, pess.email)
			# send_mail(subject, message, from_email, user.Email)
	#CONFIGURAR ESSA FUNCAOsend_mail()

	# Método sobrescrito de form_valid()
	# def form_valid(self, form):
	# 	self.object = form.save(commit=False)
	# 	Membro.objects.filter(tema_convocacao = self.object).delete()
	# 	for pessoa in form.cleaned_data['convocados']:
	# 		membro = Membro()
	# 		membro.tema_convocacao = self.object
	# 		membro.nome_pessoa = pessoa
	# 		membro.save()
	# 	return super(ModelFormMixin, self).form_valid(form)

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

#Classe Enviar e-mail
class Enviar(View):
	model = Convocacao
	template_name = 'pessoa/enviar.html'


#Classe Membro
class MembroList(ListView):
	"""
	View para listar membros cadastrados.
	"""
	model = Membro
	template_name = 'pessoa/listarmembro.html'

class MembroNew(CreateView):
	"""
	View para a criação de novos membros.
	"""
	model = Membro
	form_class = FormularioMembro
	template_name = 'pessoa/novomembro.html'
	success_url = reverse_lazy('listar-membros')

	# def envio():
	# 	conv = Convocacao()
	# 	pess = Pessoa()
	# 	memb = Membro()
	# 	# for convocado in Convocacao.objects.all():
	# 	send_mail(conv.tema, conv.pauta, settings.DEFAULT_FROM_EMAIL, memb.nome_pessoa.email)
	# envio()

	#Função envio de e-mails para os membros convocados
	# conv = Convocacao()
	# memb = Membro()
	# def send_mail(self):
	# 	subject = '[%s] Convocacao' % conv.tema
	# 	message = 'Email: %(memb.nome_pessoa.email); Pautas: %(conv.pauta)'
	# 	context = {
	# 		'email': self.cleaned_data['memb.nome_pessoa.email'],
	# 		'pautas': self.cleaned_data['conv.pauta'],
	# 	}
	# 	message = message % context
	# 	# for convocado in Convocacao.objects.all():
	# 	# 	send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, nome_pessoa.email)
	# send_mail()

class MembroEdit(UpdateView):
	"""
	View para a edição de membros já cadastrados.
	"""
	model = Membro
	form_class = FormularioMembro
	template_name = 'pessoa/editarmembro.html'
	success_url = reverse_lazy('listar-membros')

class MembroDelete(DeleteView):
	"""
	View para a exclusão de membros.
	"""
	model = Membro
	template_name = 'pessoa/deletarmembro.html'
	success_url = reverse_lazy('listar-membros')