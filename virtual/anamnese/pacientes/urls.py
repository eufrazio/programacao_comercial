from django.conf.urls import url
from pacientes import views

urlpatterns = [
   url(r'^listar/$', views.PacientesList.as_view(), name='listar-pacientes'),
   url(r'^novo/$', views.PacientesNew.as_view(), name='novo-paciente'),
   url(r'^editar/(?P<pk>[0-9]+)/$', views.PacientesEdit.as_view(), name='editar-paciente'),
   url(r'^excluir/(?P<pk>[0-9]+)/$', views.PacientesDelete.as_view(), name='deletar-paciente'),
]
