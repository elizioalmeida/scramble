from django.shortcuts import render
from .models import CPod


# Create your views here.

def inicial(request):
    cprod = CPod.objects.order_by('nome_cp')

    return render(request, 'controle/inicial.html', {'cprod': cprod})

def teste(request):
   
    return render(request, 'controle/teste.html')
	

def cprod(request):

    return render(request, 'controle/cprod.html')

