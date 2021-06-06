# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, render_to_response, reverse
from .models import CPod, CDesenvolvimento, ItemDesenvolvimento, Escopo, Tarefas
from .forms import CPForm, CDForm, ESForm, ITForm, TRForm, CDForm_novo, ESForm_novo, CPForm_novo, ITForm_novo, \
    TRForm_novo, testeForm

from django.views import generic
from django.views.generic import ListView, View
from django.views.generic.base import TemplateView

from django.http import HttpResponse, HttpResponseRedirect, FileResponse, Http404
from django.template import RequestContext, loader

from django.db.models import Count, Q, Sum, F, Aggregate, Subquery, OuterRef
from django.db import connections, connection

from .pdf import relCP, relGrafCP

import re

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login


# import io


## Listas ##
## CP ##
def cp_list(request, **proj):
    CP_ = CPod.objects.all().order_by('nome_cp')
    template = loader.get_template('controle/cpod_list.html')
    ctx = {'CProducao_list': CP_, }
    context = RequestContext(request, ctx)

    ##sql(1)

    return HttpResponse(template.render(ctx))


def cp_proj(request, **proj):
    CP_ = CPod.objects.all().order_by('nome_cp')
    template = loader.get_template('controle/cpod_proj.html')
    ctx = {'CProducao_list': CP_, }
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(ctx))


def cp_cli(request, **cli):
    CP_ = CPod.objects.all().order_by('cliente')
    template = loader.get_template('controle/cpod_cli.html')
    ctx = {'CProducao_list': CP_, }
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(ctx))


## CD ##
def cd_list(request, **proj):
    CD_ = CDesenvolvimento.objects.all().order_by('nome_cd')
    template = loader.get_template('controle/cd_list.html')
    ctx = {'CDes_list': CD_, }
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(ctx))


def cd_cpod(request, **proj):
    CD_ = CDesenvolvimento.objects.all().order_by('cpod_id')
    template = loader.get_template('controle/cd_cpod.html')
    ctx = {'CDes_list': CD_, }
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(ctx))


def cd_des(request, **proj):
    CD_ = CDesenvolvimento.objects.all().order_by('desenvolvedor')
    template = loader.get_template('controle/cd_des.html')
    ctx = {'CDesenvolvimento_list': CD_, }
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(ctx))


def cd_list_cp(request, pro):  # lista os cd por cp especifico.
    CD_ = CDesenvolvimento.objects.filter(cpod_id=pro)
    CP_ = CPod.objects.filter(id=pro)
    template = loader.get_template('controle/cd_list_cp.html')
    ctx = {
        'CDes_list': CD_,
        'CDes_pro': pro,
        'CP_list': CP_,
        'CP_pro': pro,
    }
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(ctx))


## ES ##
def es_list(request, **proj):
    ES_ = Escopo.objects.all().order_by('nome_escopo')
    template = loader.get_template('controle/es_list.html')
    ctx = {'ES_list': ES_, }
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(ctx))


def es_cpod(request, **proj):
    ES_ = Escopo.objects.all().order_by('cpod_id')
    template = loader.get_template('controle/es_cpod.html')
    ctx = {'ES_list': ES_, }
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(ctx))


def es_list_cp(request, pro):  # lista os es por cp especifico.
    ES_ = Escopo.objects.filter(cpod_id=pro)
    CP_ = CPod.objects.filter(id=pro)
    template = loader.get_template('controle/es_list_cp.html')
    ctx = {
        'ES_list': ES_,
        'ES_pro': pro,
        'CP_list': CP_,
        'CP_pro': pro,
    }
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(ctx))


## IT ##
def it_list(request, **proj):
    # tr_par = {} ver se precisa ainda
    IT_ = ItemDesenvolvimento.objects.all().order_by('nome_item')

    template = loader.get_template('controle/it_list.html')

    ctx = {'IT_list': IT_,}
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(ctx))


def it_cdes(request, **proj):
    IT_ = ItemDesenvolvimento.objects.all().order_by('cdes_id')
    template = loader.get_template('controle/it_cdes.html')
    ctx = {'IT_list': IT_, }
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(ctx))


def it_list_cd(request, pro):  # lista os Itens por CDesenv especifico.
    IT_ = ItemDesenvolvimento.objects.filter(cdes_id=pro)
    CD_ = CDesenvolvimento.objects.filter(id=pro)
    template = loader.get_template('controle/it_list_cd.html')
    ctx = {
        'IT_list': IT_,
        'IT_pro': pro,
        'CD_list': CD_,
        'CD_pro': pro,
    }
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(ctx))


## TR ##
def tr_list(request, **proj):
    TR_ = Tarefas.objects.all().order_by('nome_tarefa')
    template = loader.get_template('controle/tr_list.html')
    ctx = {'TR_list': TR_, }
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(ctx))


def tr_item(request, **proj):
    TR_ = Tarefas.objects.all().order_by('itdes_id')
    template = loader.get_template('controle/tr_itdes.html')
    ctx = {'TR_list': TR_, }
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(ctx))


def tr_list_it(request, pro):
    TR_ = Tarefas.objects.filter(itdes_id=pro)
    IT_ = ItemDesenvolvimento.objects.filter(id=pro)
    template = loader.get_template('controle/tr_list_it.html')
    ctx = {
        'TR_list': TR_,
        'TR_pro': pro,
        'IT_list': IT_,
        'IT_pro': pro,
    }
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(ctx))


##  Novo - Forms  ##
## CP ##
def cp_novo(request):
    args = {}
    if request.method == 'POST':
        form = CPForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            sql(post.pk)

            return redirect('cp_novo')  # , pk=post.pk)
        else:
            args['form'] = form
            ctx = {'cpform': form}
            return render(request, 'controle/cp_form_new.html', ctx)

    else:
        form = CPForm()

    return render(request, 'controle/cp_form_new.html', {'cpform': form})


def cp_edit(request, pk):
    post = get_object_or_404(CPod, pk=pk)
    if request.method == "POST":
        form = CPForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            sql(pk)

            return redirect('cp_edit', pk=post.pk)
    else:
        form = CPForm(instance=post)
    return render(request, 'controle/cp_form.html', {'cpform': form, 'PK': pk})


## CD ##
def cd_new(request, pk):
    post = get_object_or_404(CDesenvolvimento, pk=pk)
    args = {}
    if request.method == "POST":
        form = CDForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('cd_new', pk=post.pk)
        else:
            args['form'] = form
            ctx = {'cdform': form}
            # return render(request, "controle/teste.html", args)
            return render(request, 'controle/cd_form.html', ctx)
        # return render(request, "controle/cd_form.html", {'cdform':args})
        # return redirect('cd_new', pk=post.pk )
    else:
        form = CDForm(instance=post)
    return render(request, 'controle/cd_form.html', {'cdform': form})


def cd_novo(request, cp):
    NomeCPod = CPod.nome_cp.queryset = CPod.objects.filter(id=cp)
    args = {}
    if request.method == 'POST':
        form = CDForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.cpod_id = cp
            post.save()
            return redirect('cd_list_cp', pro=cp)

        else:
            args['form'] = form
            ctx = {'cdform': form}
            return render(request, 'controle/cd_form_new.html', ctx)
    else:
        form = CDForm_novo(cp)
    return render(request, 'controle/cd_form_new.html', {'cdform': form, 'cp': cp, 'nome_cpod': NomeCPod})


## ES ##
def es_novo(request, cp):
    NomeCPod = CPod.nome_cp.queryset = CPod.objects.filter(id=cp)
    if request.method == 'POST':
        form = ESForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.cpod_id = cp
            post.save()
            return redirect('es_list_cp', pro=cp)

    else:
        form = ESForm_novo(cp)
    return render(request, 'controle/es_form_new.html', {'esform': form, 'cp': cp, 'nome_cpod': NomeCPod})


## IT ##
def it_edit(request, pk):
    post = get_object_or_404(ItemDesenvolvimento, pk=pk)
    args = {}
    if request.method == "POST":
        form = ITForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            sql(pk)

            return redirect('it_edit', pk=post.pk)
        else:
            args['form'] = form
            ctx = {'itform': form}
            return render(request, 'controle/it_form.html', ctx)
    else:
        form = ITForm(instance=post)
    return render(request, 'controle/it_form.html', {'itform': form})


def it_novo(request, cd):
    NomeCDes = CDesenvolvimento.nome_cd.queryset = CDesenvolvimento.objects.filter(id=cd)
    args = {}
    if request.method == 'POST':
        form = ITForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.cdes_id = cd
            post.save()

            sql(cd)

            return redirect('it_list_cd', pro=cd)

        else:
            args['form'] = form
            ctx = {'cdform': form}
            return render(request, 'controle/it_form_new.html', ctx)
    else:
        form = ITForm_novo(cd)
    return render(request, 'controle/it_form_new.html', {'itform': form, 'cd': cd, 'nome_cdes': NomeCDes})


## TR ##
def tr_edit(request, pk):
    post = get_object_or_404(Tarefas, pk=pk)
    args = {}
    if request.method == "POST":
        form = TRForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            '''post.itdes_id = pk >>> estava gravando o id da tarefa no id do It de des'''
            post.save()

            sql(pk)

            return redirect( 'tr_edit', pk=post.pk)
            '''return redirect('tr_list_it', pro=post.pk)'''

        else:
            args['form'] = form
            ctx = {'trform': form}
            return render(request, 'controle/tr_form.html', ctx)
    else:
        form = TRForm(instance=post)
    return render(request, 'controle/tr_form.html', {'trform': form})


def tr_novo(request, it):
    NomeITDes = ItemDesenvolvimento.nome_item.queryset = ItemDesenvolvimento.objects.filter(id=it)
    args = {}
    if request.method == 'POST':
        form = TRForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.itdes_id = it
            post.save()

            sql(it)

            return redirect('tr_list_it', pro=it)

        else:
            args['form'] = form
            ctx = {'itform': form}
            return render(request, 'controle/tr_form_new.html', ctx)
    else:
        form = TRForm_novo(it)
    return render(request, 'controle/tr_form_new.html', {'trform': form, 'it': it, 'nome_itdes': NomeITDes})


class addcp_listview(View):
    model = CPod
    paginate_by = 10
    template_name = 'addcp_list.html'


#	def get_context_data(self, **kwargs):
#		cprod = CPod.objects.order_by('nome_cp')
#		return render(request, 'controle/addcp_list.html', {'cprod': cprod})


def sql(tk):
    # ---- Update do que esta concluido para Tarefas -----
    tr_par = Tarefas.objects.values_list('itdes_id').annotate(ttt=Sum(F('participacao') * F('status')) / 100)
    for par in (list(tr_par)):
        ItemDesenvolvimento.objects.filter(id=par[0]).update(concluido=par[1])
    # ----
    # ---- Update para ItemDesenvolvimento ----
    it_par = ItemDesenvolvimento.objects.values_list('cdes').annotate(ttt=Sum(F('participacao') * F('concluido')) / 100)
    for par in (list(it_par)):
        CDesenvolvimento.objects.filter(id=par[0]).update(status=par[1])
    # -----
    # ----- Update para CDesenvolvimento ----
    cd_par = CDesenvolvimento.objects.values_list('cpod_id').annotate(ttt=Sum(F('participacao') * F('status')) / 100)
    for par in (list(cd_par)):
        CPod.objects.filter(id=par[0]).update(status=par[1])
    # ----

    return


def cp_delete(request, pk):
    # CPod.objects.get(pk=request.DELETE['pk']).delete()
    CP_ = CPod.objects.all().order_by('nome_cp')
    template = loader.get_template('controle/cpod_list.html')
    ctx = {'CProducao_list': CP_, }
    context = RequestContext(request, ctx)

    obj = CPod.objects.get(id=pk)
    obj.delete()
    # return render(request, 'controle/cpod_list.html' CP_)
    return HttpResponse(template.render(ctx))


def es_delete(request, pk, escopo):
    ES_ = Escopo.objects.all().order_by('nome_escopo')
    template = loader.get_template('controle/es_list.html')
    ctx = {'ES_list': ES_, }
    context = RequestContext(request, ctx)

    obj = Escopo.objects.get(id=pk)
    obj.delete()

    return HttpResponse(template.render(ctx))
    #return redirect('es_list_cp', escopo)


def cd_delete(request, pk, cp):
    #CP_ = CPod.objects.all().order_by('nome_cp')
    CD_ = CDesenvolvimento.objects.all().order_by('cpod_id')
    template = loader.get_template('controle/cd_list.html')
    #ctx = {'CProducao_list': CP_, }
    ctx = { 'CDes_list':CD_, }
    context = RequestContext(request, ctx)

    obj = CDesenvolvimento.objects.get(id=pk)
    obj.delete()

    #return redirect('cd_list_cp', cp)
    return HttpResponse(template.render(ctx))


def it_delete(request, pk, cd ):
    IT_ = ItemDesenvolvimento.objects.all().order_by('nome_item')
    #CD_ = CDesenvolvimento.objects.all().order_by('cpod_id')
    template = loader.get_template('controle/it_list.html')
    # ctx = { 'CDes_list':CD_, }
    ctx = {'IT_list': IT_, }


    context = RequestContext(request, ctx)

    obj = ItemDesenvolvimento.objects.get(id=pk)
    obj.delete()

    # return redirect('it_list_cd', cd )
    return HttpResponse(template.render(ctx))


def tr_delete(request, pk, it):
    TR_ = Tarefas.objects.all().order_by('nome_tarefa')
    template = loader.get_template('controle/tr_list.html')
    ctx = { 'TR_list': TR_, }

    context = RequestContext(request, ctx)

    obj = Tarefas.objects.get(id=pk)
    obj.delete()

    return HttpResponse(template.render(ctx))


def inicial(request):
    cprod = CPod.objects.order_by('nome_cp')
    # cps = CPod.objects.filter('nome_cp')
    return render(request, 'controle/inicial.html', {'cprod': cprod})


def teste(request):
    return render(request, 'controle/teste.html')


def cprod(request):
    return render(request, 'controle/cprod.html')


def addcp(request):
    return render(request, 'controle/addcp.html')


def es_edit(request, pk):
    post = get_object_or_404(Escopo, pk=pk)
    if request.method == "POST":
        form = ESForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('es_edit', pk=post.pk)
    else:
        form = ESForm(instance=post)

    return render(request, 'controle/es_form.html', {'esform': form})


def addcp_list(request):
    cpa = CPod.objects.order_by('nome_cp')
    return render(request, 'controle/addcp.html', {'cpa': cpa})


def cpodteste(request):
    cpd = CPod.objects.order_by('nome_cp')
    return render(request, 'controle/teste.html', {'cpd': cpd})


class AboutView(TemplateView):
    template_name = "about.html"


# reportlab


def pdf_view(request):
    import sys, os, os.path
    import subprocess
    from subprocess import call

    relCP()

    '''
    name = '/home/elizio/scramble/controle/static/reports/relCP'
    diretorio = '/home/elizio/scramble/controle/static/reports/'
    proc=subprocess.Popen(['/usr/bin/pdflatex', '-output-directory', diretorio, '%s.tex'%name])
    proc.communicate()
    '''
    return FileResponse(open(os.path.dirname(__file__) + '/static/reports/relCP.pdf', 'r'),
                        content_type='application/pdf')

def pdf_view1(request):
    import sys, os, os.path
    import subprocess
    from subprocess import call

    relCP()
    

    return FileResponse(open(os.path.dirname(__file__) + '/static/reports/relCP.pdf', 'r'),
                        content_type='application/pdf')


def grafCP(request):
    import sys, os, os.path
    import subprocess
    from subprocess import call

    relGrafCP()
    
    name = '/home/elizio/scramble/controle/static/reports/relGrafCP'
    diretorio = '/home/elizio/scramble/controle/static/reports/'
    proc = subprocess.Popen(['/usr/bin/pdflatex', '-output-directory', diretorio, '%s.tex' % name])
    proc.communicate()
   
    return FileResponse(open(os.path.dirname(__file__) + '/static/reports/relGrafCP.pdf', 'r'),
                        content_type='application/pdf')

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('inicial')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'controle/cadastro.html', {'form_usuario': form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('inicial')
        else:
            form_login = AuthenticationForm()
    
    else:
        form_login = AuthenticationForm()
    return render(request, 'controle/login.html', {'form_login': form_login})

            

'''
    with open('/mnt/droplet/home/elizio/scramble/controle/templates/controle/teste.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=teste.pdf'
        return response
    pdf.closed
'''

# return render(request, 'reports/teste.pdf',)
'''
    # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'

    # Crie o objeto PDF, usando o objeto response como seu "arquivo".
    p = canvas.Canvas(response)

    # Desenhe coisas no PDF. Aqui é onde a geração do PDF acontece.
    # Veja a documentação do ReportLab para a lista completa de
    # funcionalidades.
    p.drawString(100, 100, "Hello world.")

    # Feche o objeto PDF, e está feito.
    p.showPage()
    p.save()

'''
