#-*- coding: utf-8 -*-

### models.py ###

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
    status = models.IntegerField('Progresso', default=0, blank=True, null=True)   

    class Meta:
        verbose_name = ('Cartão de Produção')
        verbose_name_plural = ('Catões de Produção')

    def __unicode__(self):
        return self.nome_cp


class Escopo(models.Model):
    cpod = models.ForeignKey(CPod, verbose_name='Cartão de Produção')
    nome_escopo = models.CharField('Escopo', max_length=50)
    descricao = models.TextField('Descrição', blank=True, null=True)

    def __unicode__(self):
        return self.nome_escopo


class CDesenvolvimento(models.Model):
    cpod = models.ForeignKey(CPod, verbose_name= 'Cartão de Produção')
    nome_cd = models.CharField('Nome do Cartão de Desenv', max_length=50)
    desenvolvedor = models.CharField('Desenvolvedor', max_length=50)
    descricao = models.TextField('Descrição', blank=True, null=True)
    data_des_ini = models.DateField('Data Desenv Início', blank=True, null=True)
    data_des_fim = models.DateField('Data Desenv Fim', blank=True, null=True)
    obs = models.TextField('Observações', blank=True, null=True)
    participacao = models.DecimalField('%', decimal_places=2, max_digits=3)

    class Meta:
        verbose_name = ('Cartão de Desenvovimento')
        verbose_name_plural = ('Cartões de Desenvolvimento')

    def __unicode__(self):
        return self.nome_cd


class ItemDesenvolvimento (models.Model):
    cdes = models.ForeignKey(CDesenvolvimento, verbose_name= 'Cartão de Desenvolvimento')
    nome_item = models.CharField('Nome do Item', max_length=50)
    descricao = models.TextField('Descrição', blank=True, null=True)
    data_ini = models.DateField('Data Início Real', blank=True, null=True)
    data_fim = models.DateField('Data Fim Real', blank=True, null=True)
    obs = models.TextField('Observações', blank=True, null=True)
    participacao = models.DecimalField('%', decimal_places=2, max_digits=3)
    concluido = models.DecimalField('% Concluído', blank=True, null=True, decimal_places=2, max_digits=3)

    class Meta:
        verbose_name = ('Item de Desenvolvimento')
        verbose_name_plural = ('Itens de Desenvolvimento')

    def __unicode__(self):
        return self.nome_item
