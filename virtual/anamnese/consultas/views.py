from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from consultas.forms import *
from consultas.models import *
from django.shortcuts import render_to_response

# Create your views here.

# class ConsultasList(ListView):
#   """
#   View para listar consultas.
#   """
#   model = Pergunta
#   template_name = 'consultas/listar.html'
#   success_url = reverse_lazy('listar-perguntas')

def diagnostico(request): #fazer logica do diagnostico aqui  
	return render(request, 'consultas/listar.html')
