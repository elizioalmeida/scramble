from django.shortcuts import render, get_object_or_404
from .models import CPod
from .forms import CPForm

from django.views.generic import ListView

# Create your views here.

class cp_listview(ListView):
	model = CPod
	paginate_by = 10
	template_name = 'cpod_list.html'

def inicial(request):
	cprod = CPod.objects.order_by('nome_cp')
	#cps = CPod.objects.filter('nome_cp')		
	return render(request, 'controle/inicial.html', {'cprod': cprod})

def teste(request):
	return render(request, 'controle/teste.html' )
	
def cprod(request):
	return render(request, 'controle/cprod.html')

def addcp(request):
	return render(request, 'controle/addcp.html')

def cp_new(request, pk):
    	form = CPForm()
	######form = get_object_or_404(CPForm(), pk=pk)
	return render(request, 'controle/cp_form.html', {'form':form})

def cp_list(request):
	cps = CPod.objects.order_by('nome_cp')
	return render(request, 'controle/cp_list.html', {'cps':cps})


