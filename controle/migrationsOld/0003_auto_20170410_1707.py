# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0002_auto_20170410_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpod',
            name='data_ini',
            field=models.DateField(verbose_name=b'Data In\xc3\xadcio'),
        ),
        migrations.AlterField(
            model_name='cpod',
            name='nome_cp',
            field=models.CharField(max_length=50, verbose_name=b'Cart\xc3\xa3o de Produ\xc3\xa7\xc3\xa3o'),
        ),
        migrations.AlterField(
            model_name='escopo',
            name='descricao',
            field=models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o'),
        ),
        migrations.AlterField(
            model_name='escopo',
            name='nome_escopo',
            field=models.CharField(max_length=50, verbose_name=b'Escopo'),
        ),
    ]
