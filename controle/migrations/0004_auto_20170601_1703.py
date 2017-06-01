# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0003_auto_20170522_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdesenvolvimento',
            name='participacao',
            field=models.DecimalField(null=True, verbose_name=b'Paricipa\xc3\xa7\xc3\xa3o', max_digits=3, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='cdesenvolvimento',
            name='cpod',
            field=models.ForeignKey(verbose_name=b'Cart\xc3\xa3o de Produ\xc3\xa7\xc3\xa3o', to='controle.CPod'),
        ),
        migrations.AlterField(
            model_name='escopo',
            name='cpod',
            field=models.ForeignKey(verbose_name=b'Cart\xc3\xa3o de Produ\xc3\xa7\xc3\xa3o', to='controle.CPod'),
        ),
    ]
