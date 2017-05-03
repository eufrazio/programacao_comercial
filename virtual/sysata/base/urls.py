from django.conf.urls import url
from base import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]


# urlpatterns = [
#     url(r'^$', views.IndexView.as_view(), name='index'),
# ]