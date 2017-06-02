# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CDesenvolvimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_cd', models.CharField(max_length=50, verbose_name=b'Nome do Cart\xc3\xa3o de Desenv')),
                ('desenvolvedor', models.CharField(max_length=50, verbose_name=b'Desenvolvedor')),
                ('descricao', models.TextField(null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True)),
                ('data_des_ini', models.DateField(null=True, verbose_name=b'Data Desenv In\xc3\xadcio', blank=True)),
                ('data_des_fim', models.DateField(null=True, verbose_name=b'Data Desenv Fim', blank=True)),
                ('obs', models.TextField(null=True, verbose_name=b'Observa\xc3\xa7\xc3\xb5es', blank=True)),
                ('participacao', models.DecimalField(verbose_name=b'%', max_digits=3, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Cart\xe3o de Desenvovimento',
                'verbose_name_plural': 'Cart\xf5es de Desenvolvimento',
            },
        ),
        migrations.CreateModel(
            name='CPod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_cp', models.CharField(max_length=50, verbose_name=b'Nome do Cart\xc3\xa3o')),
                ('cliente', models.CharField(max_length=50, verbose_name=b'Cliente')),
                ('data_ini', models.DateField(verbose_name=b'Data In\xc3\xadcio')),
                ('data_fim', models.DateField(verbose_name=b'Data Final')),
                ('data_des_ini', models.DateField(null=True, verbose_name=b'Data Desenv In\xc3\xadcio', blank=True)),
                ('data_des_fim', models.DateField(null=True, verbose_name=b'Data Desenv Final', blank=True)),
                ('obs', models.TextField(null=True, verbose_name=b'Observa\xc3\xa7\xc3\xb5es', blank=True)),
            ],
            options={
                'verbose_name': 'Cart\xe3o de Produ\xe7\xe3o',
                'verbose_name_plural': 'Cat\xf5es de Produ\xe7\xe3o',
            },
        ),
        migrations.CreateModel(
            name='Escopo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_escopo', models.CharField(max_length=50, verbose_name=b'Escopo')),
                ('descricao', models.TextField(null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True)),
                ('cpod', models.ForeignKey(verbose_name=b'Cart\xc3\xa3o de Produ\xc3\xa7\xc3\xa3o', to='controle.CPod')),
            ],
        ),
        migrations.CreateModel(
            name='ItemDesenvolvimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_item', models.CharField(max_length=50, verbose_name=b'Nome do Item')),
                ('descricao', models.TextField(null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True)),
                ('data_ini', models.DateField(null=True, verbose_name=b'Data In\xc3\xadcio Real', blank=True)),
                ('data_fim', models.DateField(null=True, verbose_name=b'Data Fim Real', blank=True)),
                ('obs', models.TextField(null=True, verbose_name=b'Observa\xc3\xa7\xc3\xb5es', blank=True)),
                ('participacao', models.DecimalField(verbose_name=b'%', max_digits=3, decimal_places=2)),
                ('concluido', models.DecimalField(null=True, verbose_name=b'% Conclu\xc3\xaddo', max_digits=3, decimal_places=2, blank=True)),
                ('cdes', models.ForeignKey(verbose_name=b'Cart\xc3\xa3o de Desenvolvimento', to='controle.CDesenvolvimento')),
            ],
            options={
                'verbose_name': 'Item de Desenvolvimento',
                'verbose_name_plural': 'Itens de Desenvolvimento',
            },
        ),
        migrations.AddField(
            model_name='cdesenvolvimento',
            name='cpod',
            field=models.ForeignKey(verbose_name=b'Cart\xc3\xa3o de Produ\xc3\xa7\xc3\xa3o', to='controle.CPod'),
        ),
    ]
