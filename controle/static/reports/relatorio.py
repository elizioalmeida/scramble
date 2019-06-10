#!/usr/bin/env python
# coding:utf-8
# -*- coding: utf_8 -*-

import sys, os, os.path
import subprocess
from subprocess import call
from datetime import datetime
#import pygtk
#pygtk.require("2.0")
#import gtk

import sqlite3
import locale
import datetime

from .. models import CPod, CDesenvolvimento, ItemDesenvolvimento, Escopo, Tarefas
from .. import views
from django.template import RequestContext, loader

#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()



#class principal:
'''Programa Relatório
    def __init__(self):
#----- Banco de Dados

        self.con = sqlite3.connect("Controle.db")
        self.conecta = self.con.cursor()
        self.con.execute('PRAGMA foreign_keys=ON')
        self.con.execute('PRAGMA encoding="UTF-8";')

        self.filename = sys.argv[0]
        self.opfile = sys.argv[0] + '.tex'
        self.outfile = open(self.opfile, 'w')
        self.a_tex_file("blunk")

	s = subprocess.call(["pdflatex", self.filename])
	os.system('evince ' + self.filename + '.pdf')
	    
'''

#def cp_list(request, **proj):
def relCP (request ): #self, title):
    CP_ = CPod.objects.all().order_by('nome_cp')
    template = loader.get_template('controle/cpod_list.html')
    ctx = { 'CProducao_list': CP_, }
    context = RequestContext(request, ctx) 
	
    #sql(1)
	
    #return HttpResponse(template.render(ctx))

    con = sqlite3.connect("/home/elizio/scramble/db.sqlite3")
    conecta = con.cursor()
    
    
    filename = sys.argv[0]
    #filename = '/home/elizio/scramble/controle/templates/reports/relCP'
    opfile = sys.argv[0] + '.tex'
    outfile = open(opfile, 'w')
    relCP("blunk")
    

    s = subprocess.call(["pdflatex", filename])
    os.system('evince ' + filename + '.pdf')
    


    
    conecta.execute("""
	SELECT nome_cp, cliente, data_ini, data_fim
	FROM controle_cpod
	ORDER BY nome_cp
			    """)
    con.commit()
    table = conecta.fetchall()
    

    #store = self.go('liststore3')
    store = []
    

    now = datetime.now()
    pageAry = []
    
    pa = pageAry.append
    
    pa('% Relatório de Projetos - Relação de Projetos.\n')
    
    pa('\\documentclass[12pt, a4paper]{article}\n')
    pa('\\usepackage[brazilian]{babel}\n')
    pa('\\usepackage[utf8]{inputenc}\n')
    pa('\\usepackage{booktabs}\n')
    pa('\\usepackage[lmargin=2.6cm, tmargin=3cm]{geometry}\n')

    pa('\\title{Relatório de Projetos}\n') 
    pa('\\vskip 2em\n\\font\\default=cmr12\n ')
    pa('\\def\\today{January 21, 2011}\n')
    pa('\\begin{document}\n')
    pa('\\maketitle\n')
    
    pa('Relação de Projetos em Processo.\\\\ \n')
    pa('================================\\\\ \n')
    
    pa('Data: ' + str(now.day) + '/ ' + str(now.month ) + '/ ' + str(now.year) + '\\\\ \n')
    pa('Hora: ' + str(now.hour) + ':' + str(now.minute) + '\\\\ \n')
    
    
    pa('\\begin{table}[!h]\n')
    pa('    \\caption{Projetos} \n')
    pa('	\\vspace{0,5cm} \n')
    pa('	\\centering \n')
    pa('	\\begin{tabular}{r||l|l|l|l} \n')
    pa('	\\hline \hline\n')
    pa('    \\rule[0mm]{0mm}{6mm}\n')
    pa('		Projeto & Cliente & Data Inicial & Data Final & Valor\\\\ [1ex] \hline \n')
    pa('    \\rule[0mm]{0mm}{5mm}\n')
    
    
    for row in table:
	pa(		str(row[1]) + '\n')
	'''
	pa('	& ' + str(row[2]) + '\n')
	pa('	& ' + str(row[3]) + '\n')
	pa('	& ' + str(row[4]) + '\n')
	pa('	& ' + str(locale.currency((row[5]), grouping=True)).replace('$', '\\$' ) + '\\\\ [1ex] \n' )
	'''
    #pa('	& 3\n')
    #pa('	& 34 \\\\ \n')
    pa('\\hline \\hline\n')
    pa('\\bottomrule\n')
    pa('\\end{tabular}\n')
    #pa('\\caption{Exemplary table}\n')
    pa('\\label{ft_tab_ex}\n')
    pa('\\end{table}\n')   
    pa('\\end{document}')

    print 'estou no for ====', pageAry
    
    for i in pageAry:
	outfile.writelines(i)
    outfile.close()
    
    #os.system('tex ' + self.opfile)
    #os.system('xdvik ' + self.filename + '.dvi& ')
    #r = subprocess.call(["latex", self.filename + ".tex"])
    return 1


if __name__ == "__main__":
    hwg = principal()
    #gtk.main()






