from django.conf.urls import url
from medicos import views

urlpatterns = [
   url(r'^listar/$', views.MedicosList.as_view(), name='listar-medicos'),
   url(r'^novo/$', views.MedicosNew.as_view(), name='novo-medico'),
   url(r'^editar/(?P<pk>[0-9]+)/$', views.MedicosEdit.as_view(), name='editar-medico'),
   url(r'^excluir/(?P<pk>[0-9]+)/$', views.MedicosDelete.as_view(), name='deletar-medico'),
]
