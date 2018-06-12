from django.conf.urls import include, url
from django.contrib import admin
from . import views


from django.conf.urls.static import static
from django.conf import settings
from django.core.urlresolvers import reverse 

urlpatterns = [

    url(r'^$', views.inicial, name='inicial'),
   	url(r'^teste$', views.teste, name='teste1'),
	url(r'^controle/cprod$', views.cprod, name='teste2'),
	url(r'^controle/cprod$', views.cprod, name='cprod'),
	url(r'^controle/addcp$', views.addcp, name='addcp'),	
	url(r'^controle/addcp_list$', views.addcp_list, name='addcp_list'),
#	url(r'^controle/cp_new$', views.cp_new, name='cp_new'),
##	url(r'^controle/$(?P<proj>\w-)/$', views.list_view, name='cp_list'),
#	url(r'^controle/cpod_list$', views.cp_listview.as_view(), name='cpod_list'),
#	url(r'^controle/cpod_list$', views.cd_listview.as_view(template_name='cpod_list.html'), name='cd_list'), #linha nova

	url(r'^controle/cpod_list$', views.list_view, name='cpod_list'),
	url(r'^controle/cd_list$', views.cd_list_view, name='cd_list'),
##	url(r'^controle/cp_list$', views.list_view, name='cp_list'),
	
	url(r'^controle/addcp$', views.addcp_listview.as_view(), name='addcp'),

	url(r'^cp_new/(?P<pk>[0-9]+)/$', views.cp_new, name='cp_new'),
	url(r'^cd_new/(?P<pk>[0-9]+)/$', views.cd_new, name='cd_new'),
#	url(r'^es_new/(?P<pk>[0-9]+)/$', views.es_new, name='es_new'),
	url(r'^controle/teste$', views.cpodteste, name='teste'),

#	url(r'^controle/(?P<proj>[-\w]+)/$', views.cp_listview, name='cp_listview'),

#	url(r'^controle/cp_form$', views.cp_listview, name='cp_form'),


]
#urlpatterns =+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
