from django.conf.urls import url
from pessoa import views


urlpatterns = [
	url(r'^listar/$', views.PessoaList.as_view(), name='listar-participantes'),
	url(r'^novo/$', views.PessoaNew.as_view(), name='novo-participante'),
	url(r'^(?P<pk>[0-9]+)/$', views.PessoaEdit.as_view(), name='editar-participante'),
	url(r'^excluir/(?P<pk>[0-9]+)/$', views.PessoaDelete.as_view(), name='deletar-participante'),
]