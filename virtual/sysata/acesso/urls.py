from django.conf.urls import url
from acesso import views

urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='login'),
]
