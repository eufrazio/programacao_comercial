# -*- coding: utf-8 -*-
from django import forms
from pacientes.models import *

class FormularioPaciente(forms.ModelForm):
  """
  Formulario para o model Medico
  """

  class Meta:
    model = Paciente
    exclude = []


  '''def __init__(self, *args, **kwargs):
    super(FormularioPaciente, self).__init__(*args, **kwargs)
    self.fields['nome'].widget.attrs['placeholder'] = 'Nome'
    self.fields['nome'].widget.attrs['size'] = '100'
    self.fields['sexo'].widget.attrs['placeholder'] = 'Sexo'
    self.fields['data_nascimento'].widget.attrs['placeholder'] = ''
    self.fields['estado_civil'].widget.attrs['placeholder'] = 'Estado Civil'
    self.fields['profissao'].widget.attrs['placeholder'] = 'Profissão'
    self.fields['endereco'].widget.attrs['placeholder'] = 'Endereço'
    self.fields['medico_responsavel'].widget.attrs['placeholder'] = 'Médico Responsável'
    self.fields['alergia'].widget.attrs['placeholder'] = 'Alergia'
    self.fields['uso_medicamento'].widget.attrs['placeholder'] = 'Medicamento'
    '''