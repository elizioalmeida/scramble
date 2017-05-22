# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_cp', models.CharField(max_length=50)),
                ('cliente', models.CharField(max_length=50)),
                ('data_ini', models.DateField(verbose_name=b'Data inicio')),
                ('data_fim', models.DateField(verbose_name=b'Data final')),
            ],
        ),
        migrations.CreateModel(
            name='Escopo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_escopo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('cpod', models.ForeignKey(to='controle.CPod')),
            ],
        ),
    ]
