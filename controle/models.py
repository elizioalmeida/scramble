#-*- coding: utf-8 -*-

### models.py ###

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

from django.db import connections, connection


# Create your models here.

class CPod(models.Model):
    nome_cp = models.CharField('Nome do Cartão', max_length=50)
    cliente = models.CharField('Cliente', max_length=50)
    data_ini = models.DateField('Data Início')
    data_fim = models.DateField('Data Final')
    data_des_ini = models.DateField('Data Desenv Início',blank=True, null=True)
    data_des_fim = models.DateField('Data Desenv Final', blank=True, null=True)
    obs = models.TextField('Observações', blank=True, null=True)
    projeto = models.CharField('Projeto', max_length=50)
    status = models.IntegerField('Progresso (%)', default=0, blank=True, null=True,
	validators=[
	    MaxValueValidator(100), MinValueValidator(0)
	    ])
    participacao = models.IntegerField('Participação(%)', default=0, blank=True, null=True,
	validators=[
	    MaxValueValidator(100), MinValueValidator(0)
	    ])
    

    class Meta:
        verbose_name = ('Cartão de Produção')
        verbose_name_plural = ('Catões de Produção')

    def __unicode__(self):
        return self.nome_cp


class Escopo(models.Model):
    cpod = models.ForeignKey(CPod, verbose_name='Cartão de Produção', on_delete=models.CASCADE)
    nome_escopo = models.CharField('Escopo', max_length=50)
    descricao = models.TextField('Descrição', blank=True, null=True)

    def __unicode__(self):
        return self.nome_escopo


class CDesenvolvimento(models.Model):
    cpod = models.ForeignKey(CPod, verbose_name= 'Cartão de Produção', on_delete=models.CASCADE,)
    nome_cd = models.CharField('Cartão de Desenvolvimento', max_length=50)
    desenvolvedor = models.CharField('Desenvolvedor', max_length=50)
    descricao = models.TextField('Descrição', blank=True, null=True)
    data_des_ini = models.DateField('Data Desenv Início', blank=True, null=True)
    data_des_fim = models.DateField('Data Desenv Fim', blank=True, null=True)
    obs = models.TextField('Observações', blank=True, null=True)
    participacao = models.IntegerField('Participação (%)', default=0, blank=True, null=True,
	validators=[
		MaxValueValidator(100),
		MinValueValidator(0)
	    ])
    status = models.IntegerField('Progresso (%)', default=0, blank=True, null=True,
	validators=[
		MaxValueValidator(100),
		MinValueValidator(0)
	])

    class Meta:
        verbose_name = ('Cartão de Desenvovimento')
        verbose_name_plural = ('Cartões de Desenvolvimento')

    def __unicode__(self):
        return self.nome_cd


class ItemDesenvolvimento (models.Model):
    cdes = models.ForeignKey(CDesenvolvimento, verbose_name= 'Cartão de Desenvolvimento', on_delete=models.CASCADE)
    nome_item = models.CharField('Nome do Item', max_length=50)
    descricao = models.TextField('Descrição', blank=True, null=True)
    data_ini = models.DateField('Data Início Real', blank=True, null=True)
    data_fim = models.DateField('Data Fim Real', blank=True, null=True)
    obs = models.TextField('Observações', blank=True, null=True)
    participacao = models.IntegerField('Participação (%)', default=0, blank=True, null=True,
	validators=[
	    MaxValueValidator(100), MinValueValidator(0)
	    ])
    concluido = models.IntegerField('Progresso (%)', default=0, blank=True, null=True,
	validators=[
	    MaxValueValidator(100), MinValueValidator(0)
	    ])

    class Meta:
        verbose_name = ('Item de Desenvolvimento')
        verbose_name_plural = ('Itens de Desenvolvimento')

    def __unicode__(self):
        return self.nome_item



class Tarefas(models.Model):
    itdes = models.ForeignKey(ItemDesenvolvimento, verbose_name='Ítem de Desenvolvimento', on_delete=models.CASCADE)
    nome_tarefa = models.CharField('Tarefa', max_length=50)
    descricao = models.TextField('Descrição', blank=True, null=True)
    data_ini = models.DateField('Data Início', blank=True, null=True)
    data_fim = models.DateField('Data Final', blank=True, null=True)
    obs = models.TextField('Observações', blank=True, null=True)
    participacao = models.IntegerField('Participação (%)', default=0, blank=True, null=True,
	validators=[
	    MaxValueValidator(100), MinValueValidator(0)
	    ])
    status = models.IntegerField('Progresso (%)', default=0, blank=True, null=True,
	    validators=[
		MaxValueValidator(100),	MinValueValidator(0)
	    ])
    class Meta:
	verbose_name = ('Tarefa')
	verbose_name_plural = ('Tarefas')
    
    def __unicode__(self):
	return self.nome_tarefa

'''

def alterar(Tarefas):
    cursor=connection.cursor()
    cursor.execute( "UPDATE Tarefas SET sataus = 11;" )
    cursor.fetchall()
    connection.commit()
'''

