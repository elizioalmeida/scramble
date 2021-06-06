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
    pa('\\usepackage{verbatim}\n')
    
    pa('\\usepackage[lmargin=0.5cm, tmargin=0.5cm]{geometry}\n')
    
    #pa('\\usepackage{pgfplots}\n')
    #pa('\\pgfplotsset{compat=newest} \n')
    pa('\\usepackage{fancyhdr}\n')
    pa('\\usepackage{caption}\n')
    pa('\\usepackage{multirow}\n')
    
    pa('\\usepackage{siunitx}\n') #% format SI units ( mas não resolveu )
    
    ##pa('\\usepackage{tabularx}\n')
    pa('\\usepackage{array, makecell}\n')
    pa('\\setcellgapes{10pt}\n')
    pa('\\usepackage[table]{xcolor}\n')
    ##pa('\\usepackage{color, colortbl}\n')
    
    pa('\\usepackage{tabu}\n')
    ##pa('\\usepackage{ltablex}\n')
    ##pa('\\usepackage{tabularx}\n')
    pa('\\usepackage{longtable}\n')
    
    ##pa('\\usepackage{xcolor}\n')
    #pa('\\usepackage[ddmmyyyy]{datetime}\n')
    
    #### --- color
    pa('  % \n')
    pa('\\definecolor{color2}{gray}{0.9}\n')
    pa('\\definecolor{CDes}{RGB}{0, 0, 255} \n')
    pa('\\definecolor{CPro}{RGB}{51, 153, 51} \n')
    pa('\\definecolor{grey2}{RGB}{250,250,250} \n')
    
    
    pa('\\title{Relatório de Cartões de Produção}\n')
    pa('\\author{elizio}\n')
    pa('\\vskip 2em \n')
    pa('\\font\\default=cmr12\n ')
    pa('\\def\\today{January 21, 2011}\n')
    
    '''
    pa('  %%% \n')
    pa(' \\fancypagestyle{style2}{ \n')
    pa(' \\renewcommand{\\footrulewidth}{0.4pt} \n')
    pa(' \\lhead{toptext} \n')
    pa(' \\chead{} \n')
    pa(' \\rhead{} \n')
    pa(' \\lfoot{docref \\newline Document uncontrolled when printed} \n')
    pa(' \\cfoot{} \n')
    pa(' \\rfoot{Version\\ 1.0\\Page\\ \\thepage} }\n')
    #pa(' } \n')
    
    pa('  %%% \n')
    '''
    
    pa('\\begin{document}\n')
    pa('\\maketitle\n')
    
    pa('\\renewcommand{\\arraystretch}{1.7} \n')
    
    pa('  % \n')
    pa('  \\begin{table}[!ht]\\centering \n')

    pa('  \\caption{Projetos}\n')
    pa('  \\caption*{ Esta é uma informação adicional para a legenda da tabela}\n')
    pa('  \\vspace{0,5cm}\n')

    pa('    % \n')
    pa('    \\centering\n')
    pa('    \\color{red}\\begin{longtabu}{p{0.1cm}c||c|c|c|c|c|c|cp{0.1cm}}\n')	
    
    p1 = '\\textbf{\\textcolor{CPro}{'
    p2 = '    &\\textbf{\\textcolor{CPro}{'
    p3 = '\\textcolor{CPro}{'
    p4 = '    &\\textcolor{CPro}{'


    
    for row in CP_:
	pa('    % \n')
	
	pa('    \\arrayrulecolor{CPro}  \n')
	pa('    \\hline \hline\n')
	pa('    \\rule[0mm]{0mm}{1mm}\n')
	
	pa('    \\multirow{2}{*}{} \n') 
	pa('    &\\renewcommand{\cellalign}{cc}\\multirow{2}{*}[-0.4cm]{' + p1 + 'Cartão Produção}}} \n') 
	pa('    \\ & \multicolumn{2}{c|}{' + p1 + 'Data Planejada}}} & \multicolumn{3}{c|}{' + p1 + '\% Desenvolvimento}}} & \multicolumn{3}{c}{' + p1 + 'Nova Previsão}}}\\\\ [1ex] \n')
	pa('    \\cline{3-10} \n')
	#pa('    \\ & & \\makecell{Inicial} & \\renewcommand{\cellalign}{lc}{Final} & Planejado & Decorrido & Perda/ Ganho & Nova Data & Ganho/Perdido & \\\\ [1ex] \hline \hline \n')
	pa('    \\ & & ' + p1 + 'Inicial}} & ' + p1 + 'Final}} & ' + p1 + 'Planejado}} & ' + p1 + 'Decorrido}} & ' + p1 + 'Perda/ Ganho }} & ' + p1 + 'Nova Data}} & ' + p1 + 'Ganho/Perdido}} & \\\\ [1ex] \hline \hline \n')
        
	##pa('    \\endhead\n')
	
	pa('    &' + p3 +	str(row.nome_cp) + '}\n')
        pa('    &' + p3 + str(row.data_ini.day).zfill(2) + '/' + str(row.data_ini.month).zfill(2) + '/' + str(row.data_ini.year) + '}\n')
        pa('    &' + p3 + str(row.data_fim.day).zfill(2) + '/' + str(row.data_fim.month).zfill(2) + '/' + str(row.data_fim.year) + '}\n')
        
	
        if(row.data_fim - row.data_ini ).days == 0: d_total = 1
        else: d_total = int((row.data_fim - row.data_ini ).days)
        d_trabalhado = int((date.today() - row.data_ini).days)
        decorrido    = int((d_trabalhado / d_total)*100)
        
	
        if row.status == 0: 
            d_falta = 0
        else:
            d_falta= int( d_trabalhado / row.status * 100)
        
        nova_data = (row.data_ini + timedelta(d_falta))
        
        pa('    &' + p3 + str(row.status) + '\\%' + ' }\n') # status
        pa('    &' + p3 + str(decorrido) + '\\%' + ' }\n') # decorrido
        pa('    &' + p3 + str(row.status - decorrido) + '\\%' + '}\n') # perda
        pa('    &' + p3 + str(nova_data.day).zfill(2) + '/' + str(nova_data.month).zfill(2) + '/' + str(nova_data.year).zfill(2) +  '}\n') 
        pa('    &' + p3 + str((row.data_fim - nova_data ).days) + '} & \\\\ [1ex] \hline \hline \n')
	pa('    \\addlinespace[2ex]\n')
	
	pa('      % \n')
	pa('      \\arrayrulecolor{CDes} \n')
	
	c1 = '\\textbf{\\textcolor{CDes}{'
	c2 = '      &\\textbf{\\textcolor{CDes}{'
	c3 = '\\textcolor{CDes}{'
	c4 = '      &\\textcolor{CDes}{'
	
	
	pa('      \\cline{2-9} \n')
	
	pa('      \n')
	
	#pa('      \\taburowcolors [1] 1{green!25 .. green!25} \n')
	
	pa('      &\\multicolumn{2}{|c||}{' + c1 + 'Cartão Desenvolvimento}}} \n')
	pa('      &\\multicolumn{2}{c|}{' + c1 + 'Desenvolvedor}}} \n')
	pa(c2 + 'Data Inicial}} \n')
	pa(c2 + 'Data Final}} \n')
	pa(c2 + 'Nova Data}} \n')
	pa('      &\\multicolumn{1}{c|}{' + c1 + 'Ganho/ Perdido}}} \\\\ [1ex] \cline{2-9} \n')
	for cd in CD_:
            if cd.cpod.id == row.id:
		
                pa('      &\\multicolumn{2}{|c||}{' + c3 + str(cd.nome_cd) + '}}\n')
                pa('      &\\multicolumn{2}{c|}{' + c3 + str(cd.desenvolvedor) + '}}\n' )
                pa(c4 + str(cd.data_des_ini.day).zfill(2) + '/' + str(cd.data_des_ini.month).zfill(2)+ '/' + str(cd.data_des_ini.year).zfill(2) + '}\n')
                pa(c4 + str(cd.data_des_fim.day).zfill(2) + '/' + str(cd.data_des_fim.month).zfill(2) +'/'+ str(cd.data_des_fim.year).zfill(2) + '}\n')
		
		if(cd.data_des_fim - cd.data_des_ini ).days == 0: cdd_total = 1
		else: cdd_total = int((cd.data_des_fim - cd.data_des_ini ).days)
        
		cdd_trabalhado = int((date.today() - cd.data_des_ini).days)
		cdd_decorrido    = int((cdd_trabalhado / cdd_total)*100)
		
		if cd.status == 0: 
		    cdd_falta = 0
		else:
		    cdd_falta= int( cdd_trabalhado / cd.status * 100)
        
		cdd_nova_data = (cd.data_des_ini + timedelta(cdd_falta))
		
		
                pa(c4 + str(cdd_nova_data.day).zfill(2) +'/' + str(cdd_nova_data.month).zfill(2) + '/'+ str(cdd_nova_data.year).zfill(2) + '}\n')
                pa('      &\\multicolumn{1}{c|}{' + c3 + str((cd.data_des_fim - cdd_nova_data).days) + '}}\\\\ [1ex] \n')
	pa('      \\cline{2-9}\\\\ \n')
	pa('      \\addlinespace[2ex]   \n')
	pa('      \\newpage \n')
	
	
    #pa('\\pagebreak \n')

    pa('\\hline \\hline\n')
    pa('\\bottomrule\\\\ \n')
    
    pa('\\end{longtabu}\n')
    #pa('\\end{center} \n')
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
