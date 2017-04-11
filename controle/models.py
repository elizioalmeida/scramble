#-*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class CPod(models.Model):
    nome_cp = models.CharField('Cartão de Produção', max_length=50)
    cliente = models.CharField('Cliente', max_length=50)
    data_ini = models.DateField('Data Início')
    data_fim = models.DateField('Data Final')

    def __unicode__(self):
        return self.nome_cp


class Escopo(models.Model):
    cpod = models.ForeignKey(CPod)
    nome_escopo = models.CharField('Escopo', max_length=50)
    descricao = models.TextField('Descrição')

    def __unicode__(self):
        return self.nome_escopo


