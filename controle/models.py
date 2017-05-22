#-*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class CPod(models.Model):
    nome_cp = models.CharField('Nome do Cartão', max_length=50)
    cliente = models.CharField('Cliente', max_length=50)
    data_ini = models.DateField('Data Início')
    data_fim = models.DateField('Data Final')
    data_des_ini = models.DateField('Data Desenv Início',blank=True, null=True)
    data_des_fim = models.DateField('Data Desenv Final', blank=True, null=True)
    obs = models.TextField('Observações', blank=True, null=True)

    class Meta:
        verbose_name = ('Cartão de Produção')
        verbose_name_plural = ('Catões de Produção')

    def __unicode__(self):
        return self.nome_cp


class Escopo(models.Model):
    cpod = models.ForeignKey(CPod)
    nome_escopo = models.CharField('Escopo', max_length=50)
    descricao = models.TextField('Descrição')

    def __unicode__(self):
        return self.nome_escopo


class CDesenvolvimento(models.Model):
    cpod = models.ForeignKey(CPod)
    nome_cd = models.CharField('Cartão de Desenvolvimento', max_length=50)
    desenvolvedor = models.CharField('Desenvolvedor', max_length=50)
    descricao = models.TextField('Descrição')

    def __unicode__(self):
        return self.nome_cd
