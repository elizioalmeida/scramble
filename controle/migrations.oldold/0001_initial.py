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
                ('nome_cd', models.CharField(max_length=50, verbose_name=b'Cart\xc3\xa3o de Desenvolvimento')),
                ('desenvolvedor', models.CharField(max_length=50, verbose_name=b'Desenvolvedor')),
                ('descricao', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
            ],
        ),
        migrations.CreateModel(
            name='CPod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_cp', models.CharField(max_length=50, verbose_name=b'Cart\xc3\xa3o de Produ\xc3\xa7\xc3\xa3o')),
                ('cliente', models.CharField(max_length=50, verbose_name=b'Cliente')),
                ('data_ini', models.DateField(verbose_name=b'Data In\xc3\xadcio')),
                ('data_fim', models.DateField(verbose_name=b'Data Final')),
            ],
        ),
        migrations.CreateModel(
            name='Escopo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_escopo', models.CharField(max_length=50, verbose_name=b'Escopo')),
                ('descricao', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('cpod', models.ForeignKey(to='controle.CPod')),
            ],
        ),
        migrations.AddField(
            model_name='cdesenvolvimento',
            name='cpod',
            field=models.ForeignKey(to='controle.CPod'),
        ),
    ]
