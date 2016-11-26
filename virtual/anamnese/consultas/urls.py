from django.conf.urls import url
from consultas import views
from django.http import HttpResponse, HttpResponseRedirect

urlpatterns = [
	url(r'^listar/$', views.ConsultasList.as_view(), name='listar-perguntas'),
	url(r'^diagnostico/$', views.diagnostico, name = 'diagnostico'),
]