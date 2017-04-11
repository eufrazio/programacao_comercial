from django.conf.urls import url
from automoveis import views

urlpatterns = [
	url(r'^$', views.AutomoveisList.as_view(), name='listar-automoveis'),
	url(r'^novo/$', views.AutomoveisNew.as_view(), name='novo-automovel'),
	url(r'^(?P<pk>[0-9]+)/$', views.AutomoveisEdit.as_view(), name='editar-automovel'),
	url(r'^excluir/(?P<pk>[0-9]+)/$', views.AutomoveisDelete.as_view(), name='deletar-automovel'),
]