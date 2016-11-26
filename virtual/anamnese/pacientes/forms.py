# -*- coding: utf-8 -*-
from django import forms
# from pacientes.models import *
# from django.forms.widgets import TextInput, DateInput, DateTimeInput, TimeInput
from django.forms import ModelForm


from .models import Paciente


# class MyDateInput(DateInput):#linha referente a classe date
#     input_type = 'date'

class DateInput(forms.DateInput):
    input_type = 'date'

class FormularioPaciente(ModelForm):
  """
  Formulario para o model Paciente
  """

  class Meta:
    model = Paciente
    exclude = []
    fields = ['nome','idade','sexo','estado_civil','profissao','endereco','medico_responsavel','alergia','uso_medicamento','data_nascimento']
    
    # widgets = {
    #         'data_nascimento': DateInput(),
    #     }
    # date = fields.data_nascimento(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

        
    # widgets = {
    #         'data_nascimento': forms.DateInput(attrs={'class':'datepicker'}),
    #     }


  def __init__(self, *args, **kwargs):
    super(FormularioPaciente, self).__init__(*args, **kwargs)
    self.fields['nome'].widget.attrs['placeholder'] = 'Nome'
    self.fields['nome'].widget.attrs['size'] = '100'
    self.fields['sexo'].widget.attrs['placeholder'] = 'Sexo'
    self.fields['data_nascimento'].widget.attrs['placeholder'] = '00/00/0000'
    # self.fields['data_nascimento'].widget = MyDateInput(attrs={'class':'date'})
    self.fields['estado_civil'].widget.attrs['placeholder'] = 'Estado Civil'
    self.fields['profissao'].widget.attrs['placeholder'] = 'Profissão'
    self.fields['endereco'].widget.attrs['placeholder'] = 'Endereço'
    self.fields['medico_responsavel'].widget.attrs['placeholder'] = 'Médico Responsável'
    self.fields['alergia'].widget.attrs['placeholder'] = 'Alergia'
    self.fields['uso_medicamento'].widget.attrs['placeholder'] = 'Medicamento'