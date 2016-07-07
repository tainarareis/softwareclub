from django.conf.urls import patterns, url
from usuarios import views

urlpatterns = patterns('',
	url(r'^solicitar/$', views.solicitar_registro, name="solicitar"),
	url(r'^registrar/$', views.registrar, name="registrar"),
	url(r'^autenticar/$', views.autenticar, name="registrar_social_auth"),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url':'/login/'}, name='logout')
)
