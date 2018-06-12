### forms.py ###

import datetime
from django.forms import ModelForm
from django import forms
from .models import CPod, CDesenvolvimento, Escopo

#from django.utils.translation import ugettext_lazy as _


class CPForm(forms.ModelForm):
		
	class Meta:
		model = CPod
		fields = ('id', 'nome_cp', 'cliente', 'projeto', 'data_ini', 'data_fim', 'data_des_ini', 'data_des_fim', 'obs', 'status')
		widgets = {
			
		        'obs': forms.Textarea(attrs={'cols':80, 'rows': 2}),
			'nome_cp': forms.Textarea(attrs={'cols':80, 'rows': 1}),
			'cliente': forms.Textarea(attrs={'cols':30, 'rows': 1}),
			}



class CDForm(forms.ModelForm):

	class Meta:
		model = CDesenvolvimento
		fields = ( 'cpod', 'nome_cd', 'desenvolvedor', 'descricao', 'data_des_ini', 'data_des_fim', 'obs', 'participacao')
		widgets = {
		              'obs': forms.Textarea(attrs={'cols':80, 'rows': 2}),
				'descricao': forms.Textarea(attrs={'cols':80, 'rows': 2}),
			}
		

class ESForm(forms.ModelForm):


	class Meta:
		model = Escopo
		fields= ( 'cpod', 'nome_escopo', 'descricao' )
		widgets= {

			}

