from django.conf.urls import url
from consultas import views
from django.http import HttpResponse, HttpResponseRedirect

urlpatterns = [
	url(r'^listar/$', views.diagnostico, name='diagnostico'),
	# url(r'^diagnostico/$', views.diagnostico, name = 'diagnostico'),
]