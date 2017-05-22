# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpod',
            name='cliente',
            field=models.CharField(max_length=50, verbose_name=b'Cliente'),
        ),
        migrations.AlterField(
            model_name='cpod',
            name='data_fim',
            field=models.DateField(verbose_name=b'Data Final'),
        ),
        migrations.AlterField(
            model_name='cpod',
            name='data_ini',
            field=models.DateField(verbose_name=b'Data Inicio'),
        ),
        migrations.AlterField(
            model_name='cpod',
            name='nome_cp',
            field=models.CharField(max_length=50, verbose_name=b'Cartao de Producao'),
        ),
    ]
