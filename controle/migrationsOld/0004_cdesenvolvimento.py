# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0003_auto_20170410_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='CDesenvolvimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_cd', models.CharField(max_length=50, verbose_name=b'Cart\xc3\xa3o de Desenvolvimento')),
                ('desenvolvedor', models.CharField(max_length=50, verbose_name=b'Desenvolvedor')),
                ('descricao', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('cpod', models.ForeignKey(to='controle.CPod')),
            ],
        ),
    ]
