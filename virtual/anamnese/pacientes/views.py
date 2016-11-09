# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from pacientes.forms import *
from pacientes.models import *

class PacientesList(ListView):
  """
  View para listar médicos cadastrados.
  """
  model = Paciente
  template_name = 'pacientes/listar.html'

class PacientesNew(CreateView):
  """
  View para a criação de novos médicos.
  """
  model = Paciente
  form_class = FormularioPaciente
  template_name = 'pacientes/novo.html'
  success_url = reverse_lazy('listar-pacientes')

class PacientesEdit(UpdateView):
  """
  View para a edição de médicos já cadastrados.
  """
  model = Paciente
  form_class = FormularioPaciente
  template_name = 'pacientes/editar.html'
  success_url = reverse_lazy('listar-pacientes')

class PacientesDelete(DeleteView):
  """
  View para a exclusão de médicos.
  """
  model = Paciente
  template_name = 'pacientes/deletar.html'
  success_url = reverse_lazy('listar-pacientes')
