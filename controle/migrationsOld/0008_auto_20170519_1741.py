# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0007_auto_20170519_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpod',
            name='data_d_fim',
        ),
        migrations.RemoveField(
            model_name='cpod',
            name='data_d_ini',
        ),
    ]
