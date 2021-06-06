#-*- coding: utf-8 -*-
from __future__ import division
import sys, os, os.path
import subprocess
from subprocess import call

import sqlite3
import locale
import datetime
from datetime import timedelta

from .models import CPod, CDesenvolvimento, ItemDesenvolvimento, Escopo, Tarefas
from django.template import RequestContext, loader
from django.http import FileResponse

from subprocess import call
from datetime import datetime, date, timedelta
import subprocess

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')



def pdf_view(request):
    CP_ = CPod.objects.all().order_by('nome_cp')
    #template = loader.get.template('controle/cpod_list.html')
    ctx = {'CProducao_list': CP_, }
    con = sqlite3.connect("/home/elizio/scramble/db.sqlite3")
    conecta = con.cursor()
    ### --- acho que não precisa ---
    ver_arq = verifica_arquivo()
    filename = ver_arq + 'relCP'
    opfile = ver_arq + 'relCP.tex'
    outfile = open( (ver_arq + 'relCP.tex'), 'w')
    ### -----------^
    #a_tex_file("blunk")
    s = subprocess.call(["pdflatex", (os.path.dirname(__file__) + '/static/reports/relCP.tex')])
    #'/home/elizio/scramble/controle/static/reports/relCP.tex' ])
    os.system('evince ' + filename + '.pdf')

    #return FileResponse(open('/home/elizio/scramble/controle/templates/reports/teste1.pdf', 'r'), content_type='application/pdf')
    return FileResponse(open(os.path.dirname(__file__) + '/static/reports/relCP.pdf', 'r'), content_type='application/pdf')

def relCP():
    CP_ = CPod.objects.all().order_by('nome_cp')
    ctx = {'CProducao_list': CP_, }

    CD_ = CDesenvolvimento.objects.all().order_by('nome_cd')

    con = sqlite3.connect("/home/elizio/scramble/db.sqlite3")
    conecta = con.cursor()
    conecta.execute("""
	SELECT nome_cp, cliente, data_ini, data_fim, status
	FROM controle_cpod
	ORDER BY nome_cp
			    """)
    con.commit()
    table = conecta.fetchall()

    outfile = open(os.path.dirname(__file__) + '/static/reports/relCP.tex', 'w')
    filename = open(os.path.dirname(__file__) + '/static/reports/relCP.pdf', 'w')
    opfile = open(os.path.dirname(__file__) + '/static/reports/relCP.tex', "w")

    now = datetime.now()
    pageAry = []
    pa = pageAry.append

    pa('% Relatório de Cartões de Produção.\n')
    pa('\\documentclass[ a4paper, landscape]{article}\n')
    pa('\\usepackage[brazil]{babel}\n')
    
    pa('\\usepackage[utf8]{inputenc}\n')
    pa('\\usepackage{booktabs}\n')
    
    pa('\\usepackage[lmargin=1cm, tmargin=1cm]{geometry}\n')
    #pa('\\usepackage{pgfplots}\n')
    #pa('\\pgfplotsset{compat=newest} \n')
    pa('\\usepackage{fancyhdr}\n')
    pa('\\usepackage{caption}\n')
    pa('\\usepackage{multirow}\n')
    pa('\\usepackage{tabularx}\n')
    pa('\\usepackage{array, makecell}\n')
    pa('\\setcellgapes{10pt}\n')
    
    pa('\\usepackage{tabu}\n')
    pa('\\usepackage{ltablex}\n')
    pa('\\usepackage{tabularx}\n')
    pa('\\usepackage{longtable}\n')
    #pa('\\usepackage[ddmmyyyy]{datetime}\n')
    
    
    '''
    pa('\\pagestyle{fancy}\n')
    pa('\\fancyhf{}\n')
    pa('\\rhead{ data: }\n')
    pa('\\lhead{Título}\n')
    pa('\\rfoot{Sudeste}\n')
    '''
    
    
    pa('\\title{Relatório de Cartões de Produção}\n')
    pa('\\author{elizio}\n')
    pa('\\vskip 2em\n\\font\\default=cmr12\n ')
    pa('\\def\\today{January 21, 2011}\n')
    pa('\\begin{document}\n')
    pa('\\maketitle\n')
    

    #pa('Relação de Projetos em Processo.\\\\ \n')
    #pa('================================\\\\ \n')

    pa('\\begin{table}[!h]\n')
    pa('\\center\n')
    
    pa('\\makegapedcells\n') # testar se ainda preciso
    
    pa('\\caption{Projetos}\n')
    pa('\\caption*{ Esta é uma informação adicional para a legenda da tabela}\n')
    pa('\\vspace{0,5cm}\n')
    
    # nao deu certopa('\\rowcolors{1}{gray}{white}\n')    
    pa('\\begin{tabu}{X[2]||X|X|l|l|l|l|l}\n')
    pa('\\hline \hline\n')
    pa('\\rule[0mm]{0mm}{1mm}\n')
        
    pa('\\multirow{2}{*}[-0.4cm]{Cartão Produção}  & \multicolumn{2}{c|}{Data Planejada} & \multicolumn{3}{c|}{\% Desenvolvimento} & \multicolumn{2}{c}{Nova Previsão}\\\\ [1ex] \n')
    pa('\\cline{2-8} \n')
    pa('  & Inicial & Final & Planejado & Decorrido & Perda/ Ganho & Nova Data & Dias Perdidos\\\\ [1ex] \hline \n')
    pa('\\rule[0mm]{0mm}{1mm}\n')
   

    '''
    for row in table:
	pa(	str(row[0]) + '\n')
	pa('    &' + str(row[1]) + '\n')
	pa('    &' + str(row[2]) + '\n')
	pa('    &' + str(row[3]) + '\n')
	pa('    &' + str(row[4]) + '\\\\ [1ex] \n')
    '''
    
    for row in CP_:
	pa(	str(row.nome_cp) + '\n')
	#pa('    &' + str(row.cliente) + '\n')
	pa('    &' + str(row.data_ini.day).zfill(2) + '/' + str(row.data_ini.month).zfill(2) + '/' + str(row.data_ini.year) + '\n')
	pa('    &' + str(row.data_fim.day).zfill(2) + '/' + str(row.data_fim.month).zfill(2) + '/' + str(row.data_fim.year) + '\n')
	
	
	if(row.data_fim - row.data_ini ).days == 0: d_total = 1
	else: d_total = int((row.data_fim - row.data_ini ).days)
	d_trabalhado = int((date.today() - row.data_ini).days)
	#d_total      = int((row.data_fim - row.data_ini ).days)
	decorrido    = int((d_trabalhado / d_total)*100)
	
	
	
	if row.status == 0: 
	    d_falta = 0
	else:
	    d_falta= int( d_trabalhado / row.status * 100)
	
	nova_data = (row.data_ini + timedelta(d_falta))
	
	
	
	'''
	dia_restante  = ((row.data_fim - date.today()).days)
	dia_decorrido = ((row.data_fim - date.today()).days)
	
	data_estimada = (row.data_ini + timedelta(dia_falta))
	dia_total = int((row.data_fim - row.data_ini ).days)
	'''
	
	'''
	
	'''
	
	
	pa('    &' + str(row.status) + '\\%' + ' \n') # status
	pa('    &' + str(decorrido) + '\\%' + ' \n') # decorrido
	
	
	pa('    &' + str(row.status - decorrido) + '\\%' + '\n') # perda
	#pa('    &' + str((row.data_fim - row.data_ini).days) + '\n')
	
	pa('    &' + str(nova_data) + '\n') 
	
	'''
	if row.status ==0:
	    pa('    &' + str( 0 ) + '\n')
	    pa('    &' + str( 0 ) + '\n')
	else:
	    
	    
	    pa('    &' + str(dia_falta) +'\n')
	    #pa('    &' + str(data_est.day).zfill(2) + '/' + str(data_est.month).zfill(2) + '/' + str(data_est.year) + '\n')
	    pa('    &' + data_est.strftime('%d/%m/%Y') + '\n')
	'''
	
	pa('    &' + str((row.data_fim - nova_data ).days) + ' \\\\ [1ex] \n')
	pa('\\hline \n')
	# interessante pa('\\addlinespace\n')
	pa(' Cartão Desenvolvimento & Desenvolvedor & Data Inicial & Data Final & Tempo Planejado & Tempo Decorrido & Dias Faltantes  & Pronto\\\\ [1ex] \hline \n')
	for cd in CD_:
	    if cd.cpod.id == row.id:
		pa( str(cd.nome_cd) + '\n')
		pa('    &' + str(cd.desenvolvedor) + '\n')
		pa('    &' + str(cd.data_des_ini) + '\n')
		pa('    &' + str(cd.data_des_fim) + '\n')
		pa('    &' + str(cd.participacao) + '\n')
		pa('    &' + str(cd.status) + '\\%' + ' \\\\ [1ex] \n')




    pa('\\hline \\hline\n')
    pa('\\bottomrule\n')
    pa('\\end{tabu}\n')
    pa('\\end{table}\n')
    

    '''
    pa('\\begin{tikzpicture} \n')
    pa('\\begin{axis}[ xlabel=anos, ylabel=coelhos] \n')

    pa('\\addplot[color=blue,mark=*] coordinates{ (1,2) (3,4) (5,6) (7,8) (9,10) }; \n')

    pa('\\end{axis}\n')
    pa('\\end{tikzpicture} \n')
    '''

    pa('\\end{document}')
   
   
    try:
	for i in pageAry:
	    outfile.writelines(i)
	outfile.close()

	name = '/home/elizio/scramble/controle/static/reports/relCP'
	diretorio = '/home/elizio/scramble/controle/static/reports/'
	proc=subprocess.Popen(['/usr/bin/pdflatex', '-output-directory', diretorio, '%s.tex'%name])
	proc.communicate()
	return
    except:
	return FileResponse(open(os.path.dirname(__file__) + '/static/reports/teste.pdf', 'r'), content_type='application/pdf')

def relGrafCP():
    con = sqlite3.connect("/home/elizio/scramble/db.sqlite3")
    conecta = con.cursor()
    conecta.execute("""
	SELECT nome_cp, cliente, data_ini, data_fim, status
	FROM controle_cpod
	ORDER BY nome_cp
			    """)
    con.commit()
    table = conecta.fetchall()

    outfile = open(os.path.dirname(__file__) + '/static/reports/relGrafCP.tex', 'w')
    filename = open(os.path.dirname(__file__) + '/static/reports/relGrafCP.pdf', 'w')
    opfile = open(os.path.dirname(__file__) + '/static/reports/relGrafCP.tex', "w")



    now = datetime.now()
    pageAry = []
    pa = pageAry.append

    pa('% Gráfico de Cartões de Produção.\n')
    pa('\\documentclass{article}\n')
    pa('\\usepackage[brazil]{babel}\n')
    pa('\\usepackage[utf8]{inputenc}\n')
    pa('\\usepackage{booktabs}\n')
    pa('\\usepackage[lmargin=2.6cm, tmargin=3cm]{geometry}\n')
    pa('\\usepackage{pgfplots}\n')

    pa('\\title{Relatório de Projetos}\n')
    pa('\\vskip 2em\n\\font\\default=cmr12\n ')
    pa('\\def\\today{January 21, 2011}\n')
    pa('\\begin{document}\n')
    pa('\\maketitle\n')

    pa('Gráfico de C. Produção em Processo.\\\\ \n')
    pa('================================\\\\ \n')

    pa('Data: ' + str(now.day).zfill(2) + '/ ' + str(now.month).zfill(2) + '/ ' + str(now.year) + '\\\\ \n')
    pa('Hora: ' + str(now.hour).zfill(2) + ':' + (str(now.minute)).zfill(2) + '\\\\ \n')

    pa('\\begin{tikzpicture} \n')
    pa('\\begin{axis}[ xlabel=anos, ylabel=coelhos] \n')

    pa('\\addplot[color=blue,mark=*] coordinates{ (1,2) (3,4) (5,6) (7,8) (9,10) }; \n')

    pa('\\end{axis}\n')
    pa('\\end{tikzpicture} \n')
    pa('\\end{document}')

    try:
	for i in pageAry:
	    outfile.writelines(i)
	outfile.close()

	name = '/home/elizio/scramble/controle/static/reports/relGrafCP'
	diretorio = '/home/elizio/scramble/controle/static/reports/'
	proc=subprocess.Popen(['/usr/bin/pdflatex', '-output-directory', diretorio, '%s.tex'%name])
	proc.communicate()
	return
    except:
	return FileResponse(open(os.path.dirname(__file__) + '/static/reports/teste.pdf', 'r'), content_type='application/pdf')






def verifica_arquivo(): #ver depois se vai usar ou então eliminar
    caminho = ((os.path.dirname(__file__) + '/static/reports/'))
    arquivo = caminho + 'relCP.tex'

    if not os.path.exists(caminho):
	os.makedirs(caminho)
    '''
    if not os.path.exists(arquivo):
	open(arquivo, 'w')
    '''
    return ( caminho )

'''
if __name__ == "__main__":
    hwg = principal()
'''
