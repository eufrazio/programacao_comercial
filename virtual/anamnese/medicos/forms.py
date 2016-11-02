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


  def __init__(self, *args, **kwargs):
    super(FormularioMedico, self).__init__(*args, **kwargs)
    self.fields['nome'].widget.attrs['placeholder'] = 'Nome'
    self.fields['nome'].widget.attrs['size'] = '100'
    self.fields['crm'].widget.attrs['placeholder'] = 'CRM'
    self.fields['especialidade'].widget.attrs['placeholder'] = 'Especialidade'
    self.fields['especialidade'].widget.attrs['size'] = '32'
    self.fields['telefone'].widget.attrs['placeholder'] = 'Telefone'
    self.fields['areamedica'].widget.attrs['placeholder'] = 'Area Médica'

