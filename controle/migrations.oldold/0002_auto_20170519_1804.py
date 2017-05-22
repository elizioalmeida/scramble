# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpod',
            name='data_des_fim',
            field=models.DateField(default='America/Sao_Paulo', verbose_name=b'Data Desenv Final'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cpod',
            name='data_des_ini',
            field=models.DateField(default=datetime.datetime(2017, 5, 19, 21, 4, 17, 359087, tzinfo=utc), verbose_name=b'Data Desenv In\xc3\xadcio'),
            preserve_default=False,
        ),
    ]
