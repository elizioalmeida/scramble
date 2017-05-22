# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0004_cdesenvolvimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpod',
            name='data_des_fim',
            field=models.DateField(default=1, verbose_name=b'Data Desenvolvimento Final'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cpod',
            name='data_des_ini',
            field=models.DateField(default=1, verbose_name=b'Data Desenvolvimento Inicial'),
            preserve_default=False,
        ),
    ]
