from django.shortcuts import render, get_object_or_404, redirect
from .models import CPod, CDesenvolvimento, ItemDesenvolvimento, Escopo
from .forms import CPForm, CDForm, ESForm

from django.views import generic
from django.views.generic import ListView

from django.http import HttpResponse
from django.template import RequestContext, loader

from django.db.models import Q

# Create your views here.



def list_view(request, **proj):
	
	CP_ = CPod.objects.all().order_by('nome_cp')
	CD_ = CDesenvolvimento.objects.all().order_by('desenvolvedor')
	ID_ = ItemDesenvolvimento.objects.all().order_by('nome_item')[:10]

	teste = CPod.objects.filter(data_ini='2017-01-01')

	template = loader.get_template('controle/cpod_list.html')
	ctx = {
		'CProducao_list': CP_,
		'CDesenvolvimento_list': CD_,
		'IDesenvolvimento_list': ID_,
		'C_teste': teste,
	}
	context = RequestContext(request, ctx) 

	return HttpResponse(template.render(ctx))


def cd_list_view(request, **proj):
	CD_ = CDesenvolvimento.objects.all().order_by('desenvolvedor')

	template = loader.get_template('controle/cd_list.html')
	ctx = {
		'CDesenvolvimento_list':CD_,
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
	return render(request, 'controle/cp_form.html', {'cpform':form})


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
	return render(request, 'controle/cd_form.html', {'cdform':form})

def es_new(request, pk):
	post = get_object_or_404(Escopo, pk=pk)
	if request.method == "POST":
		form = ESForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect( 'es_new', pk=post.pk)
	else:
		form = ESForm(instance=post)
	return render(request, 'controle/es_form.html', {'esform':form})
	

def addcp_list(request):
	cpa = CPod.objects.order_by('nome_cp')
	return render(request, 'controle/addcp.html', {'cpa':cpa})


def cpodteste(request):
	cpd = CPod.objects.order_by('nome_cp')
	return render(request, 'controle/teste.html', {'cpd':cpd})

