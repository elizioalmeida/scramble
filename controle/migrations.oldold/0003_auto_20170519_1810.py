# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0002_auto_20170519_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpod',
            name='data_des_fim',
            field=models.DateField(null=True, verbose_name=b'Data Desenv Final'),
        ),
        migrations.AlterField(
            model_name='cpod',
            name='data_des_ini',
            field=models.DateField(null=True, verbose_name=b'Data Desenv In\xc3\xadcio'),
        ),
    ]
