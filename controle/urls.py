from django.conf.urls import include, url
#from django.contrib import admin
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        url(r'^$', views.inicial),
   	url(r'^teste$', views.teste, name='teste1'),
	url(r'^controle/cprod$', views.cprod, name='teste2'),
	url(r'^controle/cprod$', views.cprod, name='cprod'),
	url(r'^controle/addcp$', views.addcp, name='addcp'),	
	url(r'^controle/cp_new$', views.cp_new, name='cp_new'),
	url(r'^controle/cp_list$', views.cp_list, name= 'cp_list'),
	url(r'^controle/cpod_list$', views.cp_listview.as_view(), name = 'cpod_list'),
	url(r'^controle/(?P<pk>[0-9]+)/$', views.cp_new, name='cp_new'),

]
#urlpatterns =+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
