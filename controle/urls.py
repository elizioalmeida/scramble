#-*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from . import views
from . import pdf
#from reports import relatorio


from django.conf.urls.static import static
from django.conf import settings
from django.core.urlresolvers import reverse 

#teste para salvar

urlpatterns = [

    url(r'^$', views.inicial, name='inicial'),

    ### Listas ###
    url(r'^controle/cp_list$', views.cp_list, name='cp_list'),
    url(r'^controle/cpod_proj$', views.cp_proj, name='cp_proj'),
    url(r'^controle/cpod_cli$', views.cp_cli, name='cp_cli'),
    url(r'^controle/cd_list$', views.cd_list, name='cd_list'),
    url(r'^controle/cd_des$', views.cd_des, name='cd_des'),
    url(r'^controle/cd_cpod$', views.cd_cpod, name='cd_cpod'),
    url(r'^controle/it_list$', views.it_list, name='it_list' ),
    url(r'^controle/it_cdes$', views.it_cdes, name='it_cdes' ),
    url(r'^controle/tr_list$', views.tr_list, name='tr_list' ),
    url(r'^controle/tr_item$', views.tr_item, name='tr_item' ),
    url(r'^controle/es_list$', views.es_list, name='es_list' ),
    url(r'^controle/es_cpod$', views.es_cpod, name='es_cpod'),
    
    url(r'^es_list_cp/(?P<pro>.+)/$', views.es_list_cp, name='es_list_cp'),
    url(r'^cd_list_cp/(?P<pro>.+)/$', views.cd_list_cp, name='cd_list_cp'),
    url(r'^it_list_cd/(?P<pro>.+)/$', views.it_list_cd, name='it_list_cd'),
    url(r'^tr_list_it/(?P<pro>.+)/$', views.tr_list_it, name='tr_list_it'),
    
    ### Foms edit ###
    url(r'^cp_edit/(?P<pk>[0-9]+)/$', views.cp_edit, name='cp_edit'),
    url(r'^cd_new/(?P<pk>[0-9]+)/$', views.cd_new, name='cd_new'),
    url(r'^es_edit/(?P<pk>[0-9]+)/$', views.es_edit, name='es_edit'),
    url(r'^it_edit/(?P<pk>[0-9]+)/$', views.it_edit, name='it_edit'),
    url(r'^tr_edit/(?P<pk>[0-9]+)/$', views.tr_edit, name='tr_edit'),

    ### Forms novo ###
    url(r'^cd_novo/(?P<cp>.+)/$', views.cd_novo, name='cd_novo'),
    url(r'^controle/cp_novo$', views.cp_novo, name='cp_novo'),
    url(r'^es_novo/(?P<cp>.+)/$', views.es_novo, name='es_novo'),
    url(r'^it_novo/(?P<cd>.+)/$', views.it_novo, name='it_novo'),
    url(r'^tr_novo/(?P<it>.+)/$', views.tr_novo, name='tr_novo'),
	
    url(r'^controle/addcp$', views.addcp_listview.as_view(), name='addcp'),
    url(r'^controle/teste$', views.cpodteste, name='teste'),
    url(r'^controle/cprod$', views.cprod, name='cprod'),
    url(r'^controle/addcp$', views.addcp, name='addcp'),	
    url(r'^controle/addcp_list$', views.addcp_list, name='addcp_list'),


    url(r'^controle/teste$', views.teste, name='teste' ),
    url(r'^controle/sql$', views.sql, name='sql' ),

    ### Delete ###
    url(r'^controle/cp_delete/(?P<pk>.+)/$', views.cp_delete, name='cp_delete'),
    url(r'^controle/cd_delete/(?P<pk>.+)/$', views.cd_delete, name='cd_delete'),
    url(r'^controle/es_delete/(?P<pk>.+)/$', views.es_delete, name='es_delete'),
    url(r'^controle/it_delete/(?P<pk>.+)/$', views.it_delete, name='it_delete'),
    url(r'^controle/tr_delete/(?P<pk>.+)/$', views.tr_delete, name='tr_delete'),
    
    ### PDF
    url(r'^controle/pdf_view', views.pdf_view, name='pdf_view'),
    url(r'^controle/grafCP', views.grafCP, name='grafCP'),
    #url(r'^controle/relCP', pdf.relCP, name='relCP'),
    
#	url(r'^controle/(?P<proj>[-\w]+)/$', views.cp_listview, name='cp_listview'),

#	url(r'^controle/cp_form$', views.cp_listview, name='cp_form'),
##	url(r'^controle/$(?P<proj>\w-)/$', views.list_view, name='cp_list'),
#	url(r'^controle/cpod_list$', views.cp_listview.as_view(), name='cpod_list'),
#	url(r'^controle/cpod_list$', views.cd_listview.as_view(template_name='cpod_list.html'), name='cd_list'), #linha nova

#	url(r'^controle/cp_new$', views.cp_new, name='cp_new'),

]
#urlpatterns =+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
