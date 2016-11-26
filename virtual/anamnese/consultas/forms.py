# -*- coding: utf-8 -*-
from django import forms
from consultas.models import *

class Perguntas(forms.ModelForm):
  """
  Formulario para o model Medico
  """

  class Meta:
    model = Pergunta
    exclude = []

  def __init__(self, *args, **kwargs):
  	super(Perguntas, self).__init__(*args, **kwargs)