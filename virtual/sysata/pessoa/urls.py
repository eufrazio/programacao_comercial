from django.conf.urls import url
from pessoa import views

urlpatterns = [
	url(r'^listar/$', views.PessoaList.as_view(), name='listar-participantes'),
	url(r'^novo/$', views.PessoaNew.as_view(), name='novo-participante'),
	url(r'^(?P<pk>[0-9]+)/$', views.PessoaEdit.as_view(), name='editar-participante'),
	url(r'^excluir/(?P<pk>[0-9]+)/$', views.PessoaDelete.as_view(), name='deletar-participante'),
	url(r'^listarconvocacao/$', views.ConvocacaoList.as_view(), name='listar-convocacoes'),
	url(r'^novaconvocacao/$', views.ConvocacaoNew.as_view(), name='nova-convocacao'),
	url(r'^editarconvocacao/(?P<pk>[0-9]+)/$', views.ConvocacaoEdit.as_view(), name='editar-convocacao'),
	url(r'^excluirconvocacao/(?P<pk>[0-9]+)/$', views.ConvocacaoDelete.as_view(), name='deletar-convocacao'),
]