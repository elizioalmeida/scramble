# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cpod',
            options={'verbose_name': 'Cart\xe3o de Produ\xe7\xe3o'},
        ),
        migrations.AddField(
            model_name='cpod',
            name='obs',
            field=models.TextField(null=True, verbose_name=b'Observa\xc3\xa7\xc3\xb5es', blank=True),
        ),
        migrations.AlterField(
            model_name='cpod',
            name='nome_cp',
            field=models.CharField(max_length=50, verbose_name=b'Nome do Cart\xc3\xa3o'),
        ),
    ]
