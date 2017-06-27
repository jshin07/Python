from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
        url(r'^register$', views.register),
        url(r'^login$', views.login),
        url(r'^logout$', views.logout),
        url(r'^post$', views.post),
        url(r'^secret$', views.secret),
        url(r'^mostpopular$', views.mostpopular, name= "mostpopular"),
        url(r'^show_mostpopular$', views.show_mostpopular, name= "show_mostpopular"),
        url(r'^secret/(?P<secret_id>\d+)$', views.secret_like, name= "like"),
]
