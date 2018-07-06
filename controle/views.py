from django.shortcuts import render, get_object_or_404, redirect
from .models import CPod, CDesenvolvimento, ItemDesenvolvimento, Escopo
from .forms import CPForm, CDForm, ESForm, CPForm_novo

from django.views import generic
from django.views.generic import ListView, View
from django.views.generic.base import TemplateView

from django.http import HttpResponse
from django.template import RequestContext, loader

from django.db.models import Count, Q

# Create your views here.



def list_view(request, **proj):
	
	CP_ = CPod.objects.all().order_by('nome_cp')
	CD_ = CDesenvolvimento.objects.all().order_by('desenvolvedor')
	ID_ = ItemDesenvolvimento.objects.all().order_by('nome_item')[:10]
	ES_ = Escopo.objects.all()

	teste = CPod.objects.values('projeto').annotate(projcount=Count('projeto'))

	template = loader.get_template('controle/cpod_list.html')
	ctx = {
		'CProducao_list': CP_,
		'CDesenvolvimento_list': CD_,
		'IDesenvolvimento_list': ID_,
		'Escopo_list': ES_,
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


def es_list_view(request, **proj):
	ES_ = Escopo.objects.all().order_by('nome_escopo')

	template = loader.get_template('controle/es_list.html')
	ctx = {
		'Escopo_list':ES_,
	}
	context = RequestContext(request, ctx)

	return HttpResponse(template.render(ctx))


class addcp_listview(View):
	model = CPod
	paginate_by = 10
	template_name = 'addcp_list.html'
	
#	def get_context_data(self, **kwargs):
#		cprod = CPod.objects.order_by('nome_cp')
#		return render(request, 'controle/addcp_list.html', {'cprod': cprod})




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


def cp_edit(request, pk):
	post = get_object_or_404(CPod, pk=pk)
	if request.method =="POST":
		form = CPForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect( 'cp_edit', pk=post.pk)
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
	
def cp_novo(request, *a):
#	post = get_object_or_404(CPod, *a)
	post = ""
	if request.method =="POST":
		form = CPForm_novo(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect( 'es-new')
	else:
		form = CPForm_novo(instance=post)	
#	form.save()
#	cpform=CPForm()
	return render(request, 'controle/teste2.html', {'cpform':form})



def es_teste(request, pro): #testar
	teste = Escopo.objects.filter(cpod_id=pro)

	template = loader.get_template('controle/es_list.html')
	ctx = {
		'teste_list':teste,
		}
	context = RequestContext(request, ctx)

	return HttpResponse(template.render(ctx))
#	return render(request, 'controle/es_list.html', {'teste':teste})


def addcp_list(request):
	cpa = CPod.objects.order_by('nome_cp')
	return render(request, 'controle/addcp.html', {'cpa':cpa})


def cpodteste(request):
	cpd = CPod.objects.order_by('nome_cp')
	return render(request, 'controle/teste.html', {'cpd':cpd})

class AboutView(TemplateView):
	template_name = "about.html"

