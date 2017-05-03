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