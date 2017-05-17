# -*- coding: utf-8 -*-
from django import forms
from pessoa.models import *

class FormularioPessoa(forms.ModelForm):
	"""
	Formulario para o model Pessoa
	"""
	class Meta:
		model = Pessoa
		exclude = []

class FormularioConvocacao(forms.ModelForm):
	"""
	Formulario para o model Convocacao
	"""
	class Meta:
		model = Convocacao
		exclude = ['convocados',]

class FormularioMembro(forms.ModelForm):
	"""
	Formulario para o model Membro
	"""
	class Meta:
		model = Membro
		exclude = []