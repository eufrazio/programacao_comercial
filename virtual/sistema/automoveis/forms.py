# -*- coding: utf-8 -*-
from django import forms
from automoveis.models import *

class FormularioAutomovel(forms.ModelForm):
	"""
	Formulario para o model Automovel
	"""

	class Meta:
		model = Automovel
		exclude = []