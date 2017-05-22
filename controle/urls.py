from django.conf.urls import include, url
#from django.contrib import admin
from . import views

urlpatterns = [
        url(r'^$', views.inicial),
   	url(r'^controle/teste', views.teste),
	url(r'^controle/cprod', views.cprod),


        ]
