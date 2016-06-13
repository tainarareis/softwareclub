
from django.conf.urls import patterns, url
from django.contrib import admin
from perfis import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^homepage$', views.homepage, name='homepage'),
    #url(r'^busca$', views.busca, name='busca'),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.exibir, name='exibir'),
	url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar')
)
