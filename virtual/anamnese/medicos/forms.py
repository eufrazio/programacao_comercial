# -*- coding: utf-8 -*-
from django import forms
from medicos.models import *

class FormularioMedico(forms.ModelForm):
  """
  Formulario para o model Medico
  """

  class Meta:
    model = Medico
    exclude = []
