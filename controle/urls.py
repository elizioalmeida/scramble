from django.conf.urls import include, url
#from django.contrib import admin
from . import views

urlpatterns = [
        url(r'^$', views.inicial),
   	url(r'^teste$', views.teste),
	url(r'^controle/cprod$', views.cprod),


        ]
