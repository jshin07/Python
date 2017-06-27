from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
        url(r'^register$', views.register),
        url(r'^login$', views.login),
        url(r'^logout$', views.logout),
        url(r'^post$', views.post),
        url(r'^secret$', views.secret),
        url(r'^mostpopular$', views.mostpopular, name= "mostpopular"),
        url(r'^secret/(?P<secretID>\d+)$', views.secret_like, name= "like"),
        url(r'^delete/(?P<secretID>\d+)$', views.secret_delete),
    ]
