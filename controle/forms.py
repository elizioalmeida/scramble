
from django import forms
from .models import CPod

class CPForm(forms.ModelForm):

	class Meta:
		model = CPod
		fields = ('id', 'nome_cp', 'cliente', 'data_ini', 'data_fim', 'data_des_ini', 'data_des_fim', 'obs', 'status')

