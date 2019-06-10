#-*- coding: utf-8 -*-
### forms.py ###

import datetime
from django.forms import ModelForm
from django import forms

from .models import CPod, CDesenvolvimento, Escopo, ItemDesenvolvimento, Tarefas

from django.forms.widgets import HiddenInput

from django.db import models


#from django.utils.translation import ugettext_lazy as _


class CPForm(forms.ModelForm):
		
	class Meta:
		model = CPod
		fields = ('id', 'nome_cp', 'cliente', 'projeto', 'data_ini',
			'data_fim', 'data_des_ini', 'data_des_fim', 'obs',
			 'participacao', 'status')
		widgets = {
			
		        'obs': forms.Textarea(attrs={'cols':80, 'rows': 2}),
			'nome_cp': forms.Textarea(attrs={'cols':80, 'rows': 1}),
			'cliente': forms.Textarea(attrs={'cols':30, 'rows': 1}),
			'status': forms.TextInput(attrs={'readonly':'readonly'}),
			}

class ESForm(forms.ModelForm):

    class Meta:
	model = Escopo
	fields= ( 'cpod', 'nome_escopo', 'descricao' )
	widgets= {
	    'descricao': forms.Textarea(attrs={'cols':80, 'rows': 2}),
	    }
	required = { 'cpod': False, }


class CDForm(forms.ModelForm):

    class Meta:
	model = CDesenvolvimento
	fields = ( 'cpod', 'nome_cd', 'desenvolvedor', 'descricao', 'data_des_ini', 'data_des_fim', 'obs', 'participacao', 'status')
	widgets = {
	        'obs'		: forms.Textarea(attrs={'cols':80, 'rows': 2}),
		'descricao'	: forms.Textarea(attrs={'cols':80, 'rows': 2}),
			
		}
	required = { 'cpod':False }
	
	#path = forms.CharField(required=False)
    
class ITForm(forms.ModelForm):

    class Meta:
	model = ItemDesenvolvimento
	fields = ( 'cdes', 'nome_item', 'descricao', 'data_ini', 'data_fim', 'obs', 'participacao', 'concluido')
	widgets = {
	        'obs'		: forms.Textarea(attrs={'cols':80, 'rows': 2}),
		'descricao'	: forms.Textarea(attrs={'cols':80, 'rows': 2}),
			
		}
	required = { 'cdes':False }
	
	
class TRForm(forms.ModelForm):
    class Meta:
	model = Tarefas
	fields = ( 'itdes', 'nome_tarefa', 'descricao', 'data_ini', 'data_fim', 'obs', 'participacao', 'status')
	widgets = {
	        'obs'		: forms.Textarea(attrs={'cols':80, 'rows': 2}),
		'descricao'	: forms.Textarea(attrs={'cols':80, 'rows': 2}),
			
		}
	required = { 'itdes':False }

class ESForm_novo(forms.ModelForm):

    class Meta:
	model = Escopo
	fields= ( 'cpod', 'nome_escopo', 'descricao' )
	
	widgets= {
	    'descricao': forms.Textarea(attrs={'cols':80, 'rows': 2 }),
	    }
	
    def __init__(self, cp, *args, **kwargs):
	super(ESForm_novo, self).__init__(*args, **kwargs)
	self.fields['cpod'].queryset = CPod.objects.filter(id=cp)
	self.fields['cpod'].initial=cp #parece que não funcionou
	#self.fields['cpod'].required=False
	#self.fields['cpod'].disable=True
	#self.fields['cpod'].select=cp

class CDForm_novo(forms.ModelForm):

    class Meta:
	model = CDesenvolvimento
	fields= ( 'cpod', 'nome_cd', 'desenvolvedor', 'descricao', 'data_des_ini', 'data_des_fim', 'obs', 'participacao', 'status' )
	
	widgets= {
	    'descricao'	: forms.Textarea(attrs={'cols':80, 'rows': 2 }),
	    'obs'	: forms.Textarea(attrs={'cols':80, 'rows': 2 }),
	    }
	required = { 'cpod':False }

    def __init__(self, cp, *args, **kwargs):
	super(CDForm_novo, self).__init__(*args, **kwargs)
	self.fields['cpod'].queryset = CPod.objects.filter(id=cp)
	self.fields['cpod'].initial=cp #aparece o nome
	#self.fields['cpod'].required=False
	#self.fields['cpod'].disable=True
	#self.fields['cpod'].select=cp

class ITForm_novo(forms.ModelForm):

    class Meta:
	model = ItemDesenvolvimento
	fields = ( 'cdes', 'nome_item', 'descricao', 'data_ini', 'data_fim', 'obs', 'participacao', 'concluido')
	widgets = {
	        'obs'		: forms.Textarea(attrs={'cols':80, 'rows': 2}),
		'descricao'	: forms.Textarea(attrs={'cols':80, 'rows': 2}),
			
		}
	required = { 'cdes':False }
    
    def __init__(self, cd, *args, **kwargs):
	super(ITForm_novo, self).__init__(*args, **kwargs)
	self.fields['cdes'].queryset = CDesenvolvimento.objects.filter(id=cd)
	self.fields['cdes'].initial=cd #aparece o nome 

class TRForm_novo(forms.ModelForm):

    class Meta:
	model = Tarefas
	fields = ( 'itdes', 'nome_tarefa', 'descricao', 'data_ini', 'data_fim', 'obs', 'participacao', 'status')
	widgets = {
	        'obs'		: forms.Textarea(attrs={'cols':80, 'rows': 2}),
		'descricao'	: forms.Textarea(attrs={'cols':80, 'rows': 2}),
			
		}
	required = { 'itdes':False }
    
    def __init__(self, it, *args, **kwargs):
	super(TRForm_novo, self).__init__(*args, **kwargs)
	self.fields['itdes'].queryset = ItemDesenvolvimento.objects.filter(id=it)
	self.fields['itdes'].initial=it #aparece o nome 	
	

class CPForm_novo(forms.ModelForm):
	class Meta:
		model = CPod
		fields = ( 'id', 'nome_cp', 'cliente', 'projeto', 'data_ini', 'data_fim', 'data_des_ini', 'data_des_fim', 'obs', 'status', 'participacao')
		 

class testeForm(forms.Form):
    
    nome_cp = forms.CharField(label='Nome // Cartão')
    cliente = forms.CharField(label='Cliente')
    data_ini = forms.DateField(label='Data Início')
    data_fim = forms.DateField(label='Data Final')
    data_des_ini = forms.DateField(label='Data Desenv Início')
    data_des_fim = forms.DateField(label='Data Desenv Final')
    obs = forms.CharField(label='Observações')
    status = forms.IntegerField(label='Progresso')
    projeto = forms.CharField(label='Projeto')


class testeFormCD(forms.Form):
	nome_cd = forms.CharField(label='Cartao')
	desenvolvedor = forms.CharField(label='Cliente')
	descricao = forms.CharField(label='Projeto')
	data_des_ini = forms.DateField(label='Data Ini')
	data_des_fim = forms.DateField(label='Data Fim')

