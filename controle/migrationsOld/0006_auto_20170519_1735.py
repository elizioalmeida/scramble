# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0005_auto_20170519_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpod',
            name='data_des_fim',
            field=models.DateField(verbose_name=b'Data Desenv Final'),
        ),
        migrations.AlterField(
            model_name='cpod',
            name='data_des_ini',
            field=models.DateField(verbose_name=b'Data Desenv Inicial'),
        ),
    ]
