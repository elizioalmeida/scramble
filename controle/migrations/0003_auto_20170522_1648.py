# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0002_auto_20170522_1319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cdesenvolvimento',
            options={'verbose_name': 'Cart\xe3o de Desenvovimento', 'verbose_name_plural': 'Cart\xf5es de Desenvolvimento'},
        ),
        migrations.AlterModelOptions(
            name='cpod',
            options={'verbose_name': 'Cart\xe3o de Produ\xe7\xe3o', 'verbose_name_plural': 'Cat\xf5es de Produ\xe7\xe3o'},
        ),
        migrations.AddField(
            model_name='cdesenvolvimento',
            name='data_des_fim',
            field=models.DateField(null=True, verbose_name=b'Data Desenv Fim', blank=True),
        ),
        migrations.AddField(
            model_name='cdesenvolvimento',
            name='data_des_ini',
            field=models.DateField(null=True, verbose_name=b'Data Desenv In\xc3\xadcio', blank=True),
        ),
        migrations.AddField(
            model_name='cdesenvolvimento',
            name='obs',
            field=models.TextField(null=True, verbose_name=b'Observa\xc3\xa7\xc3\xb5es', blank=True),
        ),
        migrations.AlterField(
            model_name='cdesenvolvimento',
            name='nome_cd',
            field=models.CharField(max_length=50, verbose_name=b'Nome do Cart\xc3\xa3o de Desenv'),
        ),
    ]
