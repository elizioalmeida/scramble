from django.shortcuts import render, get_object_or_404, redirect
from .models import CPod, CDesenvolvimento, ItemDesenvolvimento
from .forms import CPForm

from django.views import generic
from django.views.generic import ListView

from django.http import HttpResponse
from django.template import RequestContext, loader


# Create your views here.

'''
class cp_listview(ListView):
	model = CPod
	paginate_by = 10
	template_name = 'cpod_list.html'
	context_object_name = 'CProducao_list'

class cd_listview(ListView):
	model = CDesenvolvimento
	paginate_by = 10
	template_name = 'cpod_list.html'
	context_object_name = 'CDesenvolvimento_list'
'''
def list_view(request):
	
	CP_list = CPod.objects.all().order_by('nome_cp')
	CD_list = CDesenvolvimento.objects.all().order_by('nome_cd')
	ID_list = ItemDesenvolvimento.objects.all().order_by('nome_item')[:10]


	template = loader.get_template('controle/cpod_list.html')
	ctx = {
		'CProducao_list': CP_list,
		'CDesenvolvimento_list': CD_list,
		'IDesenvolvimento_list': ID_list,
	}
	context = RequestContext(request, ctx) 

	return HttpResponse(template.render(ctx))





class addcp_listview(ListView):
	model = CPod
	paginate_by = 10
	template_name = 'addcp_list.html'


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
	post = get_object_or_404(CPod, pk=pk)
	if request.method =="POST":
		form = CPForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect( 'cp_new', pk=post.pk)
	else:
		form = CPForm(instance=post)

	return render(request, 'controle/cp_form.html', {'form':form})

def cd_new(request, pk):
	post = get_object_or_404(CDesenvolvimento, pk=pk)
	if request.method == "POST":
		form = CDForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect( 'cd_new', pk=post.pk)
	else:
		form =  CDForm(instance=post)
	return render(request, 'controle/cd_form.html', {'CDform':form})



def cp_list(request):
	cps = CPod.objects.order_by('nome_cp')
	return render(request, 'controle/cp_list.html', {'cps':cps})

def addcp_list(request):
	cpa = CPod.objects.order_by('nome_cp')
	return render(request, 'controle/addcp.html', {'cpa':cpa})

def cpodteste(request):
	cpd = CPod.objects.order_by('nome_cp')
	return render(request, 'controle/teste.html', {'cpd':cpd})

