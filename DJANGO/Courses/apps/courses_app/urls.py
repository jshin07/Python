from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^destroy/(?P<id>\d+)$', views.deleteConf),
    url(r'^no$', views.no),
    url(r'^yes/(?P<id>\d+)$', views.yes),
]
