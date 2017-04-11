from django.conf.urls import url
from acesso import views

urlpatterns = [
    url(r'^$', views.login_view, name='login'),
]
